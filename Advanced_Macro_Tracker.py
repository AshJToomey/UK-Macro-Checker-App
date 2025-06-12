from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.card import MDCard


class MacroCheckerLayout(MDBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", padding=20, spacing=10, **kwargs)

        self.daily_total = {"calories": 0, "protein": 0, "fat": 0, "carbs": 0}

        # Input fields
        self.food = MDTextField(hint_text="Food name")
        self.quantity = MDTextField(hint_text="Quantity eaten (g/ml/units)", input_filter='float')
        self.label_amount = MDTextField(hint_text="Label amount (g/ml/units)", input_filter='float')
        self.calories = MDTextField(hint_text="Calories per label amount", input_filter='float')
        self.protein = MDTextField(hint_text="Protein per label amount (g)", input_filter='float')
        self.fat = MDTextField(hint_text="Fat per label amount (g)", input_filter='float')
        self.carbs = MDTextField(hint_text="Carbs per label amount (g)", input_filter='float')

        for widget in [self.food, self.quantity, self.label_amount, self.calories,
                       self.protein, self.fat, self.carbs]:
            self.add_widget(widget)

        self.button = MDRaisedButton(text="Add Food", pos_hint={"center_x": 0.5})
        self.button.bind(on_press=self.add_food)
        self.add_widget(self.button)

        self.output = MDLabel(text="Daily Total:\nCalories: 0\nProtein: 0g\nFat: 0g\nCarbs: 0g",
                              halign="center",
                              theme_text_color="Primary")
        self.add_widget(self.output)

    def add_food(self, _):
        try:
            quantity = float(self.quantity.text)
            label_amount = float(self.label_amount.text)
            factor = quantity / label_amount

            macros = {
                "calories": round(float(self.calories.text) * factor, 2),
                "protein": round(float(self.protein.text) * factor, 2),
                "fat": round(float(self.fat.text) * factor, 2),
                "carbs": round(float(self.carbs.text) * factor, 2),
            }

            for key in self.daily_total:
                self.daily_total[key] += macros[key]

            self.output.text = (
                f"[b]{self.food.text.title()} Macros:[/b]\n"
                f"Calories: {macros['calories']} kcal\n"
                f"Protein: {macros['protein']} g\n"
                f"Fat: {macros['fat']} g\n"
                f"Carbs: {macros['carbs']} g\n\n"
                f"[b]Daily Total:[/b]\n"
                f"Calories: {self.daily_total['calories']:.2f} kcal\n"
                f"Protein: {self.daily_total['protein']:.2f} g\n"
                f"Fat: {self.daily_total['fat']:.2f} g\n"
                f"Carbs: {self.daily_total['carbs']:.2f} g"
            )

            # Clear inputs
            self.food.text = ""
            self.quantity.text = ""
            self.label_amount.text = ""
            self.calories.text = ""
            self.protein.text = ""
            self.fat.text = ""
            self.carbs.text = ""

        except ValueError:
            self.output.text = "[color=#ff4444] Please enter valid numbers in all fields.[/color]"


class MacroCheckerApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Teal"
        self.theme_cls.theme_style = "Light"
        return MacroCheckerLayout()


if __name__ == "__main__":
    MacroCheckerApp().run()
