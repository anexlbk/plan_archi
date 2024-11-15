import matplotlib.pyplot as plt
import matplotlib.patches as patches

def generate_floor_plan(width, length, room_data):
    """
    Generate a basic floor plan using matplotlib.

    :param width: Total width of the floor plan
    :param length: Total length of the floor plan
    :param room_data: List of tuples with (room_name, room_width, room_length)
    """
    fig, ax = plt.subplots()
    fig.set_size_inches(10, 6)
    
    # Draw the outer boundary of the house
    ax.add_patch(patches.Rectangle((0, 0), width, length, fill=None, edgecolor='black', linewidth=2))
    ax.set_xlim(-1, width + 1)
    ax.set_ylim(-1, length + 1)
    ax.set_aspect('equal')
    plt.title("Floor Plan")
    
    current_y = 0  # Initialize y position to place rooms
    for room_name, room_width, room_length in room_data:
        # Ensure room width fits within the floor plan width
        room_width = min(room_width, width) 
        
        # Draw each room as a rectangle
        ax.add_patch(patches.Rectangle((0, current_y), room_width, room_length, fill=None, edgecolor='blue', linewidth=1.5))
        
        # Add room name label in the center of the rectangle
        plt.text(room_width / 2, current_y + room_length / 2, room_name, 
                 horizontalalignment='center', verticalalignment='center')
        
        # Update current_y for the next room
        current_y += room_length
    
    # Display the plot
    plt.show()

# Function to get room data from the user
def get_room_data():
    rooms = []
    number_of_rooms = int(input("Enter the number of rooms: "))
    
    for _ in range(number_of_rooms):
        room_name = input("Enter room name: ")
        room_area = float(input(f"Enter surface area of {room_name} in square meters: "))
        
        # Calculate room dimensions (width and length)
        room_width = float(input(f"Enter width of {room_name} in meters: "))
        room_length = room_area / room_width  # Calculate length from area and width
        
        rooms.append((room_name, room_width, room_length))
    
    return rooms

# Main program to get dimensions of the house and rooms from the user
def main():
    # Get total dimensions of the house
    house_width = float(input("Enter the width of the house in meters: "))
    house_length = float(input("Enter the length of the house in meters: "))
    
    # Get room data
    room_data = get_room_data()
    
    # Generate the floor plan
    generate_floor_plan(house_width, house_length, room_data)

# Run the program
if __name__ == "__main__":
    main()
