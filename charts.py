import plotly.express as px
from analytics import analytics


class ExpenseCharts:

    def category_pie_chart(self):
        df = analytics.category_summary()

        if df.empty:
            return None

        fig = px.pie(
            df,
            names="category",
            values="amount",
            title="Expense Distribution by Category",
            hole=0.4
        )

        fig.update_traces(textinfo="percent+label")
        return fig

    def category_bar_chart(self):
        df = analytics.category_summary()

        if df.empty:
            return None

        fig = px.bar(
            df,
            x="category",
            y="amount",
            title="Category-wise Expenses",
            text_auto=True
        )

        fig.update_layout(
            xaxis_title="Category",
            yaxis_title="Amount"
        )

        return fig

    def monthly_line_chart(self):
        df = analytics.monthly_summary()

        if df.empty:
            return None

        fig = px.line(
            df,
            x="Month",
            y="amount",
            markers=True,
            title="Monthly Expense Trend"
        )

        fig.update_layout(
            xaxis_title="Month",
            yaxis_title="Amount"
        )

        return fig


charts = ExpenseCharts()