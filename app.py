
import streamlit as st
import time

class CountdownTimerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Countdown Timer")
        
        # Set the background color of the main window
        self.root.configure(bg="#ffffff")  # Light gray background

        # Initialize variables
        self.time_left = 0
        self.running = False
        
        # Create the UI components
        self.create_widgets()

    def create_widgets(self):
        # Title label with custom font, color, and background
        self.title_label = tk.Label(self.root, text="Productivity Timer", font=("Arial", 24, "bold"), fg="#333333", bg="#f7f7f7")
        self.title_label.pack(pady=20)
        
        # Entry for time with custom font, background color, and padding
        self.time_entry = tk.Entry(self.root, font=("Arial", 18), width=5, bd=5, relief="flat", justify="center", fg="#333333", bg="#f1ebeb")  # Updated color
        self.time_entry.pack(pady=20)
        self.time_entry.insert(0, "10")  # Default 10 minutes
        
        # Countdown display label with bigger font size and custom color
        self.countdown_label = tk.Label(self.root, text="00:00", font=("Arial", 48, "bold"), fg="#ff6347", bg="#f7f7f7", width=10)
        self.countdown_label.pack(pady=20)
        
        # Frame to hold buttons for better layout
        button_frame = tk.Frame(self.root, bg="#FFFFFF")
        button_frame.pack(pady=20)

        # Start button with custom color and font
        self.start_button = tk.Button(button_frame, text="Start", font=("Arial", 14), command=self.start_timer, width=10, height=2, bg="#4caf50", fg="white", activebackground="#45a049", relief="flat")
        self.start_button.pack(side="left", padx=10)
        
        # Stop button with custom color and font
        self.stop_button = tk.Button(button_frame, text="Stop", font=("Arial", 14), command=self.stop_timer, width=10, height=2, bg="#f44336", fg="white", activebackground="#e53935", relief="flat")
        self.stop_button.pack(side="left", padx=10)
        
        # Reset button with custom color and font
        self.reset_button = tk.Button(button_frame, text="Reset", font=("Arial", 14), command=self.reset_timer, width=10, height=2, bg="#9e9e9e", fg="white", activebackground="#757575", relief="flat")
        self.reset_button.pack(side="left", padx=10)

    def start_timer(self):
        if self.running:
            return  # If it's already running, do nothing
        self.running = True
        try:
            minutes = int(self.time_entry.get())  # Using self.time_entry to get user input
            self.time_left = minutes * 60  # Convert to seconds
            self.run_countdown()
        except ValueError:
            self.show_error("Please enter a valid number")
    
    def run_countdown(self):
        if self.time_left <= 0:
            self.show_error("Time's up!")
            return
        
        minutes_left = self.time_left // 60
        seconds_left = self.time_left % 60
        self.countdown_label.config(text=f"{minutes_left:02}:{seconds_left:02}")  # Update label
        
        if self.running:
            self.time_left -= 1
            self.root.after(1000, self.run_countdown)  # Call this function again after 1 second

    def stop_timer(self):
        self.running = False
    
    def reset_timer(self):
        self.running = False
        self.time_left = 0
        self.countdown_label.config(text="00:00")
    
    def show_error(self, message):
        error_popup = tk.Toplevel(self.root)
        error_popup.title("Error")
        error_label = tk.Label(error_popup, text=message, font=("Arial", 14), fg="white", bg="#f44336")
        error_label.pack(pady=10)
        close_button = tk.Button(error_popup, text="Close", command=error_popup.destroy, bg="#f44336", fg="white", relief="flat")
        close_button.pack(pady=5)



# Set up the main window
root = tk.Tk()


app = CountdownTimerApp(root)


# Start the Tkinter event loop
root.mainloop()
