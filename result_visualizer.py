import matplotlib.pyplot as plt

class ResultVisualizer:
    def show_chart(self, result):
        labels = ["Positive", "Negative", "Neutral"]

        if result["label"] == "Positive":
            values = [100, 20, 50]
        elif result["label"] == "Negative":
            values = [50, 100, 20]
        else:
            values = [50, 20, 100]

        plt.figure()

        custom_colors = [
            "#2ecc71", #Green
            "#f39c12", # Blue
            "#3498db"  #  Light Orange
        ]

        wedges, texts, autotexts = plt.pie(
            values,
            labels=labels,
            autopct="%1.1f%%",
            startangle=90,
            colors=custom_colors,
            textprops={'color': 'white'}  # percent text
        )

        # 🔹 Side labels visible (black)
        for text in texts:
            text.set_color("black")

        plt.title("Sentiment Distribution")
        plt.axis("equal")
        plt.show()

    def emoji(self, label):
        return {}.get(label, "")
