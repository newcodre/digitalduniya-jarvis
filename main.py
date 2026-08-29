from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
import threading
import time

Window.clearcolor = (0.01, 0.01, 0.04, 1)

class DigitalDuniyaAutonomousBrain(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=30, spacing=15)
        self.header_label = Label(text="DIGITALDUNIYA AUTONOMOUS CORE", font_size='22sp', bold=True, color=(0, 0.8, 1, 1))
        self.status_label = Label(text="JARVIS: Mainframe is online, Boss. Type any robot target below:", font_size='14sp', color=(0.7, 0.7, 0.8, 1))
        self.user_input = TextInput(text="advance robot", multiline=False, font_size='16sp', size_hint=(1, 0.15), background_color=(0.1, 0.1, 0.2, 1), foreground_color=(1, 1, 1, 1))
        self.build_btn = Button(text="⚡ [ INITIATE SELF-REPLICATION ]", font_size='18sp', bold=True, background_color=(0.7, 0, 0.2, 1), size_hint=(1, 0.2))
        self.build_btn.bind(on_press=self.start_autonomous_thinking)
        self.terminal_label = Label(text="Awaiting target parameter selection...", font_size='13sp', color=(0.5, 0.5, 0.6, 1), halign='left', text_size=(Window.width - 60, None))
        layout.add_widget(self.header_label)
        layout.add_widget(self.status_label)
        layout.add_widget(self.user_input)
        layout.add_widget(self.build_btn)
        layout.add_widget(self.terminal_label)
        return layout

    def start_autonomous_thinking(self, instance):
        target = self.user_input.text.strip().lower()
        self.build_btn.text = f"[ THINKING... ]"
        self.build_btn.background_color = (0.9, 0.4, 0, 1)
        threading.Thread(target=self.generate_custom_robotics_blueprint, args=(target,)).start()

    def generate_custom_robotics_blueprint(self, target):
        time.sleep(2.0)
        if "arm" in target or "hath" in target:
            report = "🦾 ROBOTIC ARM MATRIX:\n\n1. TOPO: 3-Axis joint rotation compiled.\n2. ACTUATORS: Servo 1 (Pin 5), Servo 2 (Pin 6).\n3. CODE: Inverse kinematics tracking active."
        elif "car" in target or "gaadi" in target:
            report = "🏎️ ROVER BLUEPRINT:\n\n1. CHASSIS: 4-Wheel differential drive mesh.\n2. FIRMWARE: Motor controls ready on Pin 10, 11."
        else:
            report = f"🤖 PRODUCTION NODE FOR: {target.upper()}\n\n1. SKELTON: 3D mesh calculated.\n2. STATUS: Ready for manufacture."
        self.terminal_label.text = report
        self.build_btn.text = "⚡ [ INITIATE SELF-REPLICATION ]"
        self.build_btn.background_color = (0, 0.6, 0.4, 1)

if __name__ == '__main__':
    DigitalDuniyaAutonomousBrain().run()
  
