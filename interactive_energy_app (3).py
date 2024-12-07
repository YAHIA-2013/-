
import tkinter as tk
from tkinter import messagebox


class InteractiveApp:
    def __init__(self, root):
        self.root = root
        self.root.title("تفاعل وترشيد الطاقة")
        self.create_widgets()

    def create_widgets(self):
        # إطار العنوان
        title_frame = tk.Frame(self.root)
        title_frame.pack(pady=10)
        title_label = tk.Label(title_frame, text="تفاعل وترشيد الطاقة", font=("Helvetica", 16))
        title_label.pack()

        # إطار إدخال البيانات
        input_frame = tk.Frame(self.root)
        input_frame.pack(pady=10)

        tk.Label(input_frame, text="استهلاك الكهرباء الشهري (كيلووات ساعة):").grid(row=0, column=0, sticky='w')
        self.electricity_entry = tk.Entry(input_frame, width=30)
        self.electricity_entry.grid(row=0, column=1, pady=5)

        tk.Label(input_frame, text="كمية الماء المستخدمة يوميًا (لتر):").grid(row=1, column=0, sticky='w')
        self.water_entry = tk.Entry(input_frame, width=30)
        self.water_entry.grid(row=1, column=1, pady=5)

        tk.Label(input_frame, text="عدد الأكياس البلاستيكية المستخدمة أسبوعيًا:").grid(row=2, column=0, sticky='w')
        self.plastic_entry = tk.Entry(input_frame, width=30)
        self.plastic_entry.grid(row=2, column=1, pady=5)

        # زر الحساب
        calculate_button = tk.Button(self.root, text="احسب", command=self.calculate_usage)
        calculate_button.pack(pady=20)

    def calculate_usage(self):
        try:
            electricity = float(self.electricity_entry.get())
            water = float(self.water_entry.get())
            plastic = int(self.plastic_entry.get())

            electricity_tips = "استخدم مصابيح LED الموفرة للطاقة وقم بإطفاء الأضواء عند مغادرة الغرفة."
            water_tips = "تجنب فتح صنبور الماء بدون حاجة واغسل الملابس بالماء البارد."
            plastic_tips = "استخدم الأكياس القابلة لإعادة الاستخدام بدلاً من الأكياس البلاستيكية."

            results = f"استهلاك الكهرباء: {electricity} كيلووات ساعة شهريًا.\n"                       f"نصائح لتقليل استهلاك الكهرباء:\n- {electricity_tips}\n\n"                       f"استهلاك الماء: {water} لتر يوميًا.\n"                       f"نصائح لتقليل استهلاك الماء:\n- {water_tips}\n\n"                       f"استخدام الأكياس البلاستيكية: {plastic} كيس أسبوعيًا.\n"                       f"نصائح لتقليل استخدام البلاستيك:\n- {plastic_tips}"

            messagebox.showinfo("نتائج الحساب", results)
        except ValueError:
            messagebox.showwarning("خطأ في الإدخال", "من فضلك أدخل قيم صحيحة لجميع الحقول.")


if __name__ == "__main__":
    root = tk.Tk()
    app = InteractiveApp(root)
    root.mainloop()
