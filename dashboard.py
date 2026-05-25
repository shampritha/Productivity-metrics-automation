import streamlit as st
import pandas as pd
import glob
import plotly.express as px

st.autorefresh(
    interval=10000,
    key="dashboard_refresh"
)

# Page Configuration
st.set_page_config(
    page_title="Productivity Metrics Dashboard",
    layout="wide"
)

# Dashboard Title
st.title(
    "Productivity Metrics Dashboard"
)


# Find latest report
files = glob.glob(
    "output/*.xlsx"
)

latest_file = max(
    files,
    key=lambda x: x
)

# Load Excel Sheets
summary_df = pd.read_excel(
    latest_file,
    sheet_name="Ticket Summary"
)

productivity_df = pd.read_excel(
    latest_file,
    sheet_name="Productivity"
)
# =========================
# SIDEBAR FILTERS
# =========================

st.sidebar.header(
    "Dashboard Filters"
)

selected_employee = st.sidebar.selectbox(
    "Select Employee",
    ["All"] +
    list(summary_df["Assigned To"].unique())
)
# Apply Filter

filtered_df = summary_df.copy()

if selected_employee != "All":

    filtered_df = summary_df[
        summary_df["Assigned To"]
        == selected_employee
    ]

# =========================
# KPI METRICS
# =========================

total_closed = summary_df["Closed"].sum()

total_inprogress = summary_df["In Progress"].sum()

total_tickets = (
    total_closed +
    total_inprogress
)

# KPI Cards
col1, col2, col3 = st.columns(3)

col1.metric(
    "Total Tickets",
    total_tickets
)

col2.metric(
    "Closed Tickets",
    total_closed
)

col3.metric(
    "In Progress",
    total_inprogress
)

# =========================
# TICKET SUMMARY TABLE
# =========================

st.subheader(
    "Ticket Summary"
)

st.dataframe(filtered_df)

# =========================
# PRODUCTIVITY TABLE
# =========================

st.subheader(
    "Team Productivity"
)

st.dataframe(productivity_df)

# =========================
# PRODUCTIVITY CHART
# =========================

st.subheader(
    "Closed Tickets Chart"
)

chart_data = summary_df.set_index(
    "Assigned To"
)[["Closed", "In Progress"]]

st.bar_chart(chart_data)
# =========================
# PIE CHART
# =========================

st.subheader(
    "Ticket Distribution"
)

pie_data = pd.DataFrame({
    "Status": [
        "Closed",
        "In Progress"
    ],
    "Count": [
        total_closed,
        total_inprogress
    ]
})

fig = px.pie(
    pie_data,
    names="Status",
    values="Count",
    title="Overall Ticket Status"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# =========================
# TEAM COMPARISON
# =========================

st.subheader(
    "Team Comparison"
)

comparison_chart = px.bar(
    summary_df,
    x="Assigned To",
    y=["Closed", "In Progress"],
    barmode="group",
    title="Team Ticket Comparison"
)

st.plotly_chart(
    comparison_chart,
    use_container_width=True
)

# =========================
# GENERATED IMAGE CHART
# =========================

st.subheader(
    "Generated Productivity Dashboard"
)

st.image(
    "reports/team_productivity.png"
)

# =========================
# DOWNLOAD REPORT
# =========================

with open(latest_file, "rb") as file:

    st.download_button(
        label="Download Excel Report",
        data=file,
        file_name="team_report.xlsx",
        mime=(
            "application/vnd.openxmlformats"
            "-officedocument.spreadsheetml.sheet"
        )
    )