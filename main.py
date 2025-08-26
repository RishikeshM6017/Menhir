import dearpygui.dearpygui as dpg

# Initialize Dear PyGui
dpg.create_context()

# --- Your Application Logic and UI Definition ---

# Function to handle button click
def button_callback(sender, app_data, user_data):
    print(f"Button '{sender}' clicked! Data: {app_data}, User Data: {user_data}")
    # Example: change text on button click
    dpg.set_value("my_text_item", "Hello from Callback!")

# Create a window
with dpg.window(label="Task Planner", width=800, height=600):
    dpg.add_text("Welcome to your Task Planner!", tag="my_text_item")
    dpg.add_button(label="Click Me", callback=button_callback, user_data="Some extra info")

    # Example: A simple input text field
    dpg.add_input_text(label="Task Title", default_value="New Task")

    # Example: A checkbox
    dpg.add_checkbox(label="Completed", default_value=False)

    # You'll build out your Kanban and Gantt UI here
    # For now, just a placeholder for future sections
    dpg.add_separator()
    dpg.add_text("Kanban Board goes here...")
    dpg.add_text("Gantt Chart goes here...")

# --- Dear PyGui Configuration and Start ---

# Set up the viewport (the actual window that appears)
dpg.create_viewport(title='My Custom Title', width=1000, height=700)
dpg.setup_dearpygui() # Initializes the backend

# Show the viewport
dpg.show_viewport()

# Start the Dear PyGui render loop
# This function blocks until the application is closed
dpg.start_dearpygui()

# Clean up
dpg.destroy_context()