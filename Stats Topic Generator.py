import random
import tkinter as tk


class RandomTopicGenerator(tk.Tk):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.stats_topics = {1: "Two-Tailed T-test of Correlation Significance",
                             2: "Discrete Binomial Probability",
                             3: "Estimation of Population Means",
                             4: "Two-tailed T-test of Sample means assuming equal variance",
                             5: "Two-tailed T-test of Sample means assuming unequal variance",
                             6: "Two-tailed T-test of Sample means using matched pair design",
                             7: "Chi-Squared",
                             8: "Poisson Distribution",
                             9: "Simple Linear Regression",
                             10: "Multiple Liner Regression",
                             11: "Simple Logistics Regression",
                             12: "Multiple Logistics Regression",
                             13: "Estimation of Values",
                             14: "Backwards Stepwise Regression",
                             15: "Wilcoxon Rank-Sum"}

        self.geometry("650x150")
        self.title("Random Daily Statistics Topic!")

        rand_button = tk.Button(self, text=f'Click here to get your topic', command=self.return_topic)

        rand_button.grid(row=1, column=0)

    def return_topic(self):

        rand_value = random.randint(1, 15)

        random_topic = self.stats_topics.get(rand_value)

        stat_label = tk.Label(self, text=f"Your applied stats topic of the day is: {random_topic}")

        stat_label.grid(row=0, column=0, sticky='ew')


root = RandomTopicGenerator()

root.mainloop()
