import tkinter as tk
import math
# Initialize the tkinter root window
root = tk.Tk()
root.title("Drawing a Black Box")

# Create a canvas object
canvas = tk.Canvas(root, width=1400, height=1400, bg="white")
canvas.pack()

# Draw a black box (rectangle)
x1, y1 = -100, 600  # Top-left corner
x2, y2 = 600, 800  # Bottom-right corner
canvas.create_rectangle(x1, y1, x2, y2, fill="black")
x1, y1 = 600, 600  # Top-left corner
x2, y2 = 800, 800  # Bottom-right corner
canvas.create_rectangle(x1, y1, x2, y2, fill="purple")

x1, y1 = 800, 600  # Top-left corner
x2, y2 = 1400, 800  # Bottom-right corner
canvas.create_rectangle(x1, y1, x2, y2, fill="black")



x1, y1 = 800, 645  # Top-left corner
x2, y2 = 1400, 655  # Bottom-right corner
canvas.create_rectangle(x1, y1, x2, y2, fill="white")

x1, y1 = -100, 745  # Top-left corner
x2, y2 = 600, 755  # Bottom-right corner
canvas.create_rectangle(x1, y1, x2, y2, fill="white")
def draw_dashes(x,y,rev,rotate):
    if rotate == False:
        if rev == False:
            for i in range(0,15):
                x1, y1 = i*40+x, y-5  # Top-left corner
                x2, y2 = i*40+x+20, y+5  # Bottom-right corner
                canvas.create_rectangle(x1, y1, x2, y2, fill="white")
        else:
            for i in range(0,15):
                x1, y1 = i*-40+x, y-5  # Top-left corner
                x2, y2 = i*-40+x-20, y+5  # Bottom-right corner
                canvas.create_rectangle(x1, y1, x2, y2, fill="white")
    else:
        if rev == False:
            for i in range(0,15):
                x1, y1 = x-5, i*40+y  # Top-left corner
                x2, y2 = x+5, i*40+y+20  # Bottom-right corner
                canvas.create_rectangle(x1, y1, x2, y2, fill="white")
        else:
            for i in range(0,15):
                x1, y1 = x-5, i*-40+y  # Top-left corner
                x2, y2 = x+5, i*-40+y-20 # Bottom-right corner
                canvas.create_rectangle(x1, y1, x2, y2, fill="white")


draw_dashes(800,700, False, False)
draw_dashes(800,750, False, False)
draw_dashes(600,650,True, False)
draw_dashes(600,700,True, False)


x1, y1 = 600, -100  # Top-left corner
x2, y2 = 800, 600  # Bottom-right corner
canvas.create_rectangle(x1, y1, x2, y2, fill="black")

x1, y1 = 600, 800  # Top-left corner
x2, y2 = 800, 1400  # Bottom-right corner
canvas.create_rectangle(x1, y1, x2, y2, fill="black")



x1, y1 = 728, 800  # Top-left corner
x2, y2 = 739, 1400  # Bottom-right corner
canvas.create_rectangle(x1, y1, x2, y2, fill="white")

x1, y1 = 663, -100  # Top-left corner
x2, y2 = 672, 600  # Bottom-right corner
canvas.create_rectangle(x1, y1, x2, y2, fill="white")
draw_dashes(733,600, True, True)
draw_dashes(668,800, False, True)

canvas.create_arc(500, 715, 550, 755, start=0, extent=80, style=tk.ARC, outline="white", width=7)

# Draw a line to complete the arrow
canvas.create_line(550, 735, 550, 745, arrow=tk.LAST, fill="white", width=7)

canvas.create_arc(900, 655, 850, 685, start=180, extent=80, style=tk.ARC, outline="white", width=7)

# Draw a line to complete the arrow
canvas.create_line(850, 670, 850, 660, arrow=tk.LAST, fill="white", width=7)

canvas.create_arc(710, 540, 650, 580, start=280, extent=80, style=tk.ARC, outline="white", width=7)
canvas.create_line(685, 580, 675, 580, arrow=tk.LAST, fill="white", width=7)

canvas.create_arc(730, 820, 690, 880, start=90, extent=80, style=tk.ARC, outline="white", width=7)
canvas.create_line(710, 820, 720, 820, arrow=tk.LAST, fill="white", width=7)
class TrafficLight:
    def __init__(self, canvas, x, y, has_right_turn=False, has_left_turn=False):
        """
        Initialize a traffic light object.

        Args:
            canvas: The tkinter canvas object to draw on.
            x, y: The top-left corner coordinates of the traffic light.
            has_right_turn: Boolean indicating whether the traffic light has a right-turn arrow.
            has_left_turn: Boolean indicating whether the traffic light has a left-turn arrow.
        """
        self.canvas = canvas
        self.x = x
        self.y = y
        self.has_right_turn = has_right_turn
        self.has_left_turn = has_left_turn
        self.light_width = 20
        self.light_height = 60
        self.light_gap = 5
        self.light_colors = ["red", "yellow", "green"]
        self.arrow_colors = ["yellow", "green"]
        self.lights = {}
        self.arrows = {}
        self.current_light = "Red"
        self.current_right_arrow = "off"
        self.current_right_arrow = "off"


        # Draw main traffic light housing
        self.lights["housing"] = self.canvas.create_rectangle(x, y, x + self.light_width, y + self.light_height, fill="grey")

        # Draw main traffic lights (red, yellow, green)
        for i, color in enumerate(self.light_colors):
            light_y = y + i * (self.light_width + self.light_gap) + self.light_gap
            self.lights[color] = self.canvas.create_oval(x + self.light_gap, light_y, x + self.light_gap + self.light_width - 2 * self.light_gap, light_y + self.light_width - 2 * self.light_gap, fill="black")

        if has_right_turn:
            # Draw right-turn arrow housing
            right_light_x = x + self.light_width + self.light_gap
            self.arrows["right_housing"] = self.canvas.create_rectangle(right_light_x, y + self.light_gap + 20, right_light_x + 15, y + 40 + 20, fill="grey")

            # Draw right-turn arrow lights (yellow arrow, green arrow)
            for i, color in enumerate(self.arrow_colors):
                right_light_y = y + 25 + i * (15 + self.light_gap) + self.light_gap
                self.arrows[color + "_right"] = self.canvas.create_oval(right_light_x + self.light_gap, right_light_y, right_light_x + self.light_gap + 15 - 2 * self.light_gap, right_light_y + 15 - 2 * self.light_gap, fill="black")
                arrow_color = "white" if color == "green" else "black"
                arrow_direction = self.canvas.create_line(right_light_x + self.light_gap + 2, right_light_y + 8, right_light_x + self.light_gap + 7, right_light_y + 13, arrow=tk.LAST, fill=arrow_color, width=2)
                self.arrows[color + "_right_arrow"] = arrow_direction

        if has_left_turn:
            # Draw left-turn arrow housing
            left_light_x = x - self.light_width - self.light_gap
            self.arrows["left_housing"] = self.canvas.create_rectangle(left_light_x, y + self.light_gap + 20, left_light_x + 15, y + 40 + 20, fill="grey")

            # Draw left-turn arrow lights (yellow arrow, green arrow)
            for i, color in enumerate(self.arrow_colors):
                left_light_y = y + 25 + i * (15 + self.light_gap) + self.light_gap
                self.arrows[color + "_left"] = self.canvas.create_oval(left_light_x + self.light_gap, left_light_y, left_light_x + self.light_gap + 15 - 2 * self.light_gap, left_light_y + 15 - 2 * self.light_gap, fill="black")
                arrow_color = "white" if color == "green" else "black"
                arrow_direction = self.canvas.create_line(left_light_x + self.light_gap + 7, left_light_y + 8, left_light_x + self.light_gap + 2, left_light_y + 13, arrow=tk.LAST, fill=arrow_color, width=2)
                self.arrows[color + "_left_arrow"] = arrow_direction

    def set_light(self, light_state):
        """
        Set the main traffic light state.

        Args:
            light_state: "red", "yellow", or "green"
        """
        self.current_light = light_state
        for color in self.light_colors:
            fill_color = color if color == light_state else "black"
            self.canvas.itemconfig(self.lights[color], fill=fill_color)

    def set_right_arrow(self, arrow_state):
        """
        Set the right-turn arrow state.

        Args:
            arrow_state: "yellow", "green", or "off"
        """
        if not self.has_right_turn:
            return
        self.current_right_arrow = arrow_state
        for color in self.arrow_colors:
            fill_color = color if color == arrow_state else "black"
            self.canvas.itemconfig(self.arrows[color + "_right"], fill=fill_color)

    def set_left_arrow(self, arrow_state):
        """
        Set the left-turn arrow state.

        Args:
            arrow_state: "yellow", "green", or "off"
        """
        
        if not self.has_left_turn:
            return
        self.current_left_arrow = arrow_state
        for color in self.arrow_colors:
            fill_color = color if color == arrow_state else "black"
            self.canvas.itemconfig(self.arrows[color + "_left"], fill=fill_color)

    def set_light_and_arrows(self, light_state, right_arrow_state="off", left_arrow_state="off"):
        """
        Set both the main traffic light and the turn arrow states.

        Args:
            light_state: "red", "yellow", or "green"
            right_arrow_state: "yellow", "green", or "off"
            left_arrow_state: "yellow", "green", or "off"
        """
        self.set_light(light_state)
        self.set_right_arrow(right_arrow_state)
        self.set_left_arrow(left_arrow_state)
class Car:
    def __init__(self, canvas, x, y, color="red", turning="None", maxspeed=3, angle=0, traffic_light=None):
        """
        Initialize a car object.

        Args:
            canvas: The tkinter canvas object to draw on.
            x, y: The initial position of the car (top-left corner).
            color: The color of the car.
            turning: The direction the car intends to turn ("Left", "Right", "None").
            maxspeed: Maximum speed of the car.
            angle: The initial angle of the car.
        """
        self.active = True
        self.canvas = canvas
        self.x = x
        self.y = y
        self.color = color
        self.turning = turning
        self.indicator = False
        self.maxspeed = maxspeed
        self.speed = maxspeed
        self.angle = angle
        self.width = 20
        self.height = 30
        self.timer = 0
        self.image = self.canvas.create_polygon(self.get_car_polygon_coords(), fill=self.color)
        self.direction = 0  # Rotation angle
        self.traffic_light = traffic_light
        self.collision_box = None  # Initialize collision box as None
        self.right_turn_collision_box = None

    def get_car_polygon_coords(self):
        """
        Get the coordinates of the car's polygon shape based on the current position and angle.

        Returns:
            List of flattened coordinates representing the polygon points.
        """
        half_width = self.width / 2
        half_height = self.height / 2
        # Calculate rectangle points
        points = [
            (-half_width, -half_height),
            (half_width, -half_height),
            (half_width, half_height),
            (-half_width, half_height)
        ]
        rotated_points = [self.rotate_point(x, y, self.angle) for (x, y) in points]
        translated_points = [(self.x + x, self.y + y) for (x, y) in rotated_points]
        return [coord for point in translated_points for coord in point]

    def draw(self):
        """
        Draw the car on the canvas with its indicator if applicable.
        """
        self.canvas.coords(self.image, *self.get_car_polygon_coords())

        # Draw collision detection box
        self.update_collision_box()

    def rotate_point(self, x, y, angle):
        """
        Rotate a point around the origin by the given angle (degrees).

        Args:
            x, y: Coordinates of the point to rotate.
            angle: The angle to rotate by (degrees).

        Returns:
            (new_x, new_y): Rotated point coordinates.
        """
        angle_rad = math.radians(angle)
        new_x = x * math.cos(angle_rad) - y * math.sin(angle_rad)
        new_y = x * math.sin(angle_rad) + y * math.cos(angle_rad)
        return new_x, new_y

    def accelerate(self):
        """
        Increase the car's speed (accelerate).
        """

        #print(self.speed)
        #print(self.maxspeed)
        if self.speed > self.maxspeed:
            self.speed-=0.1
        else:
            self.speed = min(self.speed + 0.1, self.maxspeed)

    def brake(self):
        """
        Decrease the car's speed (brake).
        """

        self.speed = max(self.speed - 0.1, 0)

    def move(self):
        """
        Update the car's position based on its speed and angle.
        """
        self.y += self.speed * math.cos(math.radians(self.angle))
        self.x -= self.speed * math.sin(math.radians(self.angle))

        self.draw()

    def turn_right(self, target_angle = None):
        """
        Turn the car to the right.
        """

        #print(target_angle)
        if target_angle != None:
            if target_angle > (self.angle - 4) % 360 and target_angle < (self.angle + 4) % 360:
                self.angle = target_angle
                #print(target_angle)
                return
            self.angle = (self.angle - 4) % 360


    def turn_left(self, target_angle = None):
        """
        Turn the car to the right.
        """
        if target_angle != None:
            if target_angle > (self.angle - 4) % 360 and target_angle < (self.angle + 4) % 360:
                self.angle = target_angle
                #print("left")
                #print(target_angle)
                return

        self.angle = (self.angle + 4) % 360

    def update_collision_box(self):
        """
        Update the collision detection box in front of the car.
        """
        box_length = 100  # Length of the collision detection box
        box_width = 40  # Width of the collision detection box
        half_width = box_width / 2

        points = [
            (0, -half_width),
            (box_length, -half_width),
            (box_length, half_width),
            (0, half_width)
        ]

        rotated_points = [self.rotate_point(x, y, self.angle+90) for (x, y) in points]
        translated_points = [(self.x + x, self.y + y) for (x, y) in rotated_points]
        flat_points = [coord for point in translated_points for coord in point]

        if self.collision_box:
            self.canvas.coords(self.collision_box, *flat_points)
        else:
            #print("made")
            self.collision_box = self.canvas.create_polygon(*flat_points, outline="blue", fill="", width=1)

    def check_for_collision(self, cars):
        """
        Check for collision with the car in front using the collision box and brake if necessary.

        Args:
            cars: List of all car objects to check against.
        """
        breaking = False
        if not self.collision_box:
            return

        box_coords = self.canvas.coords(self.collision_box)

        def point_in_box(point):
            """
            Check if a point is inside the collision box.
            """
            def is_left(p0, p1, p2):
                return (p1[0] - p0[0]) * (p2[1] - p0[1]) - (p2[0] - p0[0]) * (p1[1] - p0[1])

            sign = None
            for i in range(4):
                p0 = (box_coords[2 * i], box_coords[2 * i + 1])
                p1 = (box_coords[2 * ((i + 1) % 4)], box_coords[2 * ((i + 1) % 4) + 1])
                current_sign = is_left(p0, p1, point)
                if sign is None:
                    sign = current_sign
                elif sign * current_sign < 0:
                    return False
            return True

        for other_car in cars:
            if other_car is not self:
                other_center = (other_car.x, other_car.y)
                if point_in_box(other_center):
                    breaking = True

        if breaking == True:
            #print("break")

            self.brake()     
    def update_right_turn_collision_box(self):
        """
        Create or update the right-turn collision box.
        """
        if self.turning != "Right":
            return  # Only use this box when turning right
        
        box_length = 80  # Longer length to check further ahead
        box_width = 400
        offset = 20  # Rightward offset from the center of the car
        xoffset = -70  # Rightward offset from the center of the car

        points = [
            (0+xoffset, offset), 
            (box_length+xoffset, offset), 
            (box_length+xoffset, offset + box_width), 
            (0+xoffset, offset + box_width)
        ]
        rotated_points = [self.rotate_point(x, y, self.angle) for (x, y) in points]
        translated_points = [(self.x + x, self.y + y) for (x, y) in rotated_points]

        if self.right_turn_collision_box:
            self.canvas.coords(self.right_turn_collision_box, *[coord for point in translated_points for coord in point])
        else:
            self.right_turn_collision_box = self.canvas.create_polygon(*[coord for point in translated_points for coord in point], outline="green", fill="", width=1)

    def check_right_turn_collision(self, cars):
        if not self.right_turn_collision_box:
            return False

        box_coords = self.canvas.coords(self.right_turn_collision_box)
        # return any(self.point_in_box((car.x, car.y), box_coords) for car in cars if car != self)
        breaking = False

        def point_in_box(point):
            """
            Check if a point is inside the collision box.
            """
            def is_left(p0, p1, p2):
                return (p1[0] - p0[0]) * (p2[1] - p0[1]) - (p2[0] - p0[0]) * (p1[1] - p0[1])

            sign = None
            for i in range(4):
                p0 = (box_coords[2 * i], box_coords[2 * i + 1])
                p1 = (box_coords[2 * ((i + 1) % 4)], box_coords[2 * ((i + 1) % 4) + 1])
                current_sign = is_left(p0, p1, point)
                if sign is None:
                    sign = current_sign
                elif sign * current_sign < 0:
                    return False
            return True

        for other_car in cars:
            if other_car is not self:
                other_center = (other_car.x, other_car.y)
                if point_in_box(other_center):
                    if other_car.turning == "None":
                        if other_car.traffic_light.current_light != "red":
                            breaking = True
                    elif other_car.turning == "Right":
                        if self.traffic_light.has_right_turn == False:
                            if other_car.traffic_light.current_light != "red":
                                breaking = True
                        elif other_car.traffic_light.current_light != "red" or other_car.traffic_light.current_right_arrow != "red":
                            breaking = True
                    elif other_car.turning == "Left":
                        if self.traffic_light.has_left_turn == False:
                            if other_car.traffic_light.current_light != "red":
                                breaking = True
                        elif other_car.traffic_light.current_light != "red" or other_car.traffic_light.current_left_arrow != "red":
                            breaking = True
                    if other_car.speed != 0:
                        breaking = True

        if breaking == True:
            #print("break")

            self.brake()    
    def remove_right_turn_collision_box(self):
        if self.right_turn_collision_box:
            self.canvas.delete(self.right_turn_collision_box)
            self.right_turn_collision_box = None
        # else:
        #     if self.turning == "None":
        #         if self.traffic_light and self.traffic_light.current_light == "green":
        #             self.accelerate()
        #         elif self.traffic_light and self.traffic_light.current_light == "red":
        #             self.brake()
        #     elif self.turning == "Right":
        #         if self.traffic_light.has_right_turn == False:
        #             if self.traffic_light and self.traffic_light.current_light == "green":
        #                 self.accelerate()
        #             elif self.traffic_light and self.traffic_light.current_light == "red":
        #                 self.brake()
        #         else:
        #             if self.traffic_light and self.traffic_light.current_right_arrow == "green":
        #                 self.accelerate()
        #             if self.traffic_light and self.traffic_light.current_right_arrow == "red":
        #                 self.accelerate()
        #             elif self.traffic_light and self.traffic_light.current_light == "red":
        #                 self.brake()
        #     elif self.turning == "Left":
        #         if self.traffic_light.has_right_turn == False:
        #             if self.traffic_light and self.traffic_light.current_light == "green":
        #                 self.accelerate()
        #             elif self.traffic_light and self.traffic_light.current_light == "red":
        #                 self.brake()
        #         else:
        #             if self.traffic_light and self.traffic_light.current_left_arrow == "green":
        #                 self.accelerate()
        #             if self.traffic_light and self.traffic_light.current_left_arrow == "red":
        #                 self.accelerate()
        #             elif self.traffic_light and self.traffic_light.current_light == "red":
        #                 self.brake()
        return
class CarController:
    def __init__(self, car, path):
        """
        Initialize the CarController with a car and a path of waypoints.
        
        Args:
            car (Car): The car object this controller will manage.
            path (list): A list of (x, y) tuples representing the waypoints the car should follow.
        """
        self.stopping = False
        self.active = True
        self.car = car
        self.path = path
        self.current_step = 0
        self.draw_waypoints()

    def update(self):
        """
        Update the car's position and heading based on the path.
        """
        if self.current_step < len(self.path):
            next_x, next_y = self.path[self.current_step]
            self.navigate_to(next_x, next_y)
        else:
            # Optionally, stop the car or loop the path


            self.car.active = False
            self.active = False
            # self.current_step = 0  # Uncomment to loop the path

    def navigate_to(self, target_x, target_y):
        """
        Navigate the car to the next waypoint by setting the appropriate heading.
        """

        dx = target_x - self.car.x
        dy = target_y - self.car.y
        distance = math.sqrt(dx**2 + dy**2)
        if self.current_step == 0 and self.car.turning == "Left" and distance < 200:
            self.car.maxspeed = 1
            #print("slwo")
        if self.current_step == 0 and distance < 250:
            if self.car.turning == "None":
                if self.car.traffic_light and self.car.traffic_light.current_light == "green":
                    self.car.accelerate()
                if self.car.traffic_light and self.car.traffic_light.current_light == "yellow":
                    self.car.accelerate()
                elif self.car.traffic_light and self.car.traffic_light.current_light == "red":
                    self.car.brake()
            if self.car.turning == "Left":
                if self.car.traffic_light.has_left_turn:
                    if self.car.traffic_light and self.car.traffic_light.current_left_arrow== "green":
                        self.car.accelerate()
                        #print("trying")
                    elif self.car.traffic_light and self.car.traffic_light.current_left_arrow == "yellow":
                        self.car.accelerate()
                    elif self.car.traffic_light and self.car.traffic_light.current_left_arrow == "red":
                        self.car.brake()
                    elif self.car.traffic_light and self.car.traffic_light.current_light == "green":
                        self.car.accelerate()
                    elif self.car.traffic_light and self.car.traffic_light.current_light == "yellow":
                        self.car.accelerate()
                    elif self.car.traffic_light and self.car.traffic_light.current_light == "red":
                        self.car.brake()
                else:
                    if self.car.traffic_light and self.car.traffic_light.current_light == "green":
                        self.car.accelerate()
                    elif self.car.traffic_light and self.car.traffic_light.current_light == "yellow":
                        self.car.accelerate()
                    elif self.car.traffic_light and self.car.traffic_light.current_light == "red":
                        self.car.brake()
            if self.car.turning == "Right":
                if self.car.traffic_light.has_right_turn:
                    if self.car.traffic_light and self.car.traffic_light.current_Right_arrow== "green":
                        self.car.accelerate()
                        #print("trying")
                    elif self.car.traffic_light and self.car.traffic_light.current_Right_arrow == "yellow":
                        self.car.accelerate()
                    elif self.car.traffic_light and self.car.traffic_light.current_Right_arrow == "red":
                        self.car.brake()
                    elif self.car.traffic_light and self.car.traffic_light.current_light == "green":
                        self.car.accelerate()
                    elif self.car.traffic_light and self.car.traffic_light.current_light == "yellow":
                        self.car.accelerate()
                    elif self.car.traffic_light and self.car.traffic_light.current_light == "red":
                        self.car.brake()
                else:
                    if self.car.traffic_light and self.car.traffic_light.current_light == "green":
                        self.car.accelerate()
                    elif self.car.traffic_light and self.car.traffic_light.current_light == "yellow":
                        self.car.accelerate()
                    elif self.car.traffic_light and self.car.traffic_light.current_light == "red":
                        self.car.brake()

        else:
            self.car.accelerate()

        
        if self.current_step == 1 and self.car.turning == "Left":
            self.car.maxspeed = 0.5
        elif self.current_step == 1 and self.car.turning == "Right":
            if self.car.traffic_light.has_right_turn:
                if self.car.traffic_light.current_Right_arrow != "green" and self.car.traffic_light.current_Right_arrow != "yellow":
                    self.car.update_right_turn_collision_box()
            else:
                self.car.update_right_turn_collision_box()
            self.car.maxspeed = 1

            #print("slow")
        elif self.current_step == 2 and self.car.turning == "Right":
            self.car.remove_right_turn_collision_box()
            self.car.maxspeed = 1
            #print("slow")
        else:
            self.car.maxspeed = 3
        if distance > 20:  # Set a threshold to avoid small oscillations at the waypoint
            # Calculate the angle to the target and normalize it    
            angle_to_target = math.degrees(math.atan2(dy, dx))
            #print("totar")
            #print(angle_to_target+180)
            #print((self.car.angle-90+360)%360)
            angle_to_target = ((angle_to_target + 180) % 360)  # Normalize angle between 0 and 360
            # Calculate the difference and adjust the direction based on the shortest turning path
            angle_diff = (angle_to_target - self.car.angle-90+360) % 360

            #print(angle_to_target)
            #print(self.car.angle)

            if angle_diff > 182:
                # Turn left if the shortest path is to rotate counter-clockwise
                #self.car.angle -= min((360 - angle_diff), self.car.maxspeed)
                #self.car.turn_right(angle_to_target)
                self.car.turn_left(angle_to_target)

            elif angle_diff<178:
                # Turn right if the shortest path is to rotate clockwise
                #self.car.angle += min(angle_diff, self.car.maxspeed)
                #self.car.turn_left(angle_to_target)
                self.car.turn_right(angle_to_target)

            self.car.angle %= 360  # Normalize angle to stay within 0-360 degrees

        else:
            self.current_step += 1  # Move to the next waypoint if close enough

    def draw_waypoints(self):
        """
        Draw circles on the canvas at each waypoint.
        """
        for x, y in self.path:
            self.car.canvas.create_oval(x - 5, y - 5, x + 5, y + 5, fill='red', outline='white')




# def drive():
#     """
#     Update all car controllers.
#     """
#     for controller in car_controllers:
#         controller.update()
#     root.after(50, drive)  # Schedule next update

# Draw traffic lights as objects
top_left = TrafficLight(canvas, 550, 530)
top_right = TrafficLight(canvas, 830, 530, has_left_turn=True)
bottom_left = TrafficLight(canvas, 550, 820)
bottom_right = TrafficLight(canvas, 820, 820, has_right_turn=True)

# Example usage to set lights and arrows 
top_left.set_light_and_arrows("green", "off", "off")
top_right.set_light_and_arrows("yellow", "yellow", "off")
bottom_left.set_light_and_arrows("red", "off", "yellow")
bottom_right.set_light_and_arrows("red", "off", "off")
cars = []

for i in range(0,0):
    cars.append(Car(canvas, x=i*-50+00, y=675, angle=270, traffic_light=top_left))


# Draw a line to complete the arrow
# canvas.create_line(850, 670, 850, 660, arrow=tk.LAST, fill="white", width=7)
# Start the tkinter event loop
top_left.set_light("red")
top_right.set_light("red")
top_right.set_left_arrow("red")
bottom_left.set_light("green")
paths = [
    [(600, 675), (775, 625), (1600,625)],
    [(800, 725), (600, 775), (-200,775)],
    [(767, 600), (767, 800), (767,1600)],
    [(633, 800), (633, 600), (633,-200)],
    [(767, 585), (800, 625), (1600,625)],
    [(800, 675), (725, 675), (633, 600), (633,-200)],
    [(633, 815), (600, 775), (-200,775)],
    [(585, 625), (633, 600), (633,-200)],
    [(825, 775), (766, 800), (766,1600)],
    [(700, 800), (700, 700), (800, 625), (1600,625)],
    [(700, 600), (700, 700), (600, 775), (-200,775)],
    [(600, 725), (700, 725), (766, 800), (766,1600)]
    
]




# Create CarController instances

controllers = [CarController(car, paths[0]) for car in cars]
tempcars = []
for i in range(0,10):
    tempcars.append(Car(canvas, x=i*50+1400, y=725, angle=90, traffic_light=bottom_right))
for car in tempcars:
    controllers.append(CarController(car,paths[1]))
cars += tempcars
# tempcars = []
# for i in range(0,10):
#     tempcars.append(Car(canvas, x=767, y=i*-50, angle=0, traffic_light=top_right))
# for car in tempcars:
#     controllers.append(CarController(car,paths[2]))
# cars += tempcars
# tempcars = []
# for i in range(0,10):
#     tempcars.append(Car(canvas, x=633, y=i*50+1400, angle=180, traffic_light=bottom_left))
# for car in tempcars:
#     controllers.append(CarController(car,paths[3]))
# cars += tempcars

# tempcars = []
# for i in range(0,10):
#     tempcars.append(Car(canvas, x=767, y=i*-50, angle=0, traffic_light=top_right, turning = "Left"))
# for car in tempcars:
#     controllers.append(CarController(car,paths[4]))
# cars += tempcars

# tempcars = []
# for i in range(0,10):
#     tempcars.append(Car(canvas, x=633, y=i*50+1400, angle=180, traffic_light=bottom_left, turning = "Left"))
# for car in tempcars:
#     controllers.append(CarController(car,paths[6]))
# cars += tempcars
# tempcars = []
# for i in range(0,10):
#     tempcars.append(Car(canvas, x=i*-50, y=625, angle=270, traffic_light=top_left, turning = "Left"))
# for car in tempcars:
#     controllers.append(CarController(car,paths[7]))
# cars += tempcars

# tempcars = []
# for i in range(0,10):
#     tempcars.append(Car(canvas, x=1400+i*50, y=775, angle=90, traffic_light=bottom_right, turning = "Left"))
# for car in tempcars:
#     controllers.append(CarController(car,paths[8]))
# cars += tempcars


# tempcars = []
# for i in range(0,10):
#     tempcars.append(Car(canvas, x=i*50+1400, y=675, angle=90, traffic_light=top_right, turning = "Right"))
# for car in tempcars:
#     controllers.append(CarController(car,paths[5]))
# cars += tempcars

# tempcars = []
# for i in range(0,10):
#     tempcars.append(Car(canvas, x=700, y=i*50+1400, angle=180, traffic_light=bottom_left, turning = "Right"))
# for car in tempcars:
#     controllers.append(CarController(car,paths[9]))
# cars += tempcars

# tempcars = []
# for i in range(0,10):
#     tempcars.append(Car(canvas, x=700, y=i*-50, angle=0, traffic_light=bottom_left, turning = "Right"))
# for car in tempcars:
#     controllers.append(CarController(car,paths[10]))
# cars += tempcars
tempcars = []
for i in range(0,10):
    tempcars.append(Car(canvas, x=i*-50, y=725, angle=270, traffic_light=bottom_left, turning = "Right"))
for car in tempcars:
    controllers.append(CarController(car,paths[11]))
cars += tempcars
def animate():
    active_controllers  = [controller for controller in controllers if controller.active]
    if active_controllers :  # Only continue if there are active controllers
        for controller in active_controllers :
            controller.update()
        root.after(50, animate)
    else:
        print("All cars have completed their paths.")

def drive(car):
    """
    Update the car's movement, acceleration, and turning.
    """
    if car.right_turn_collision_box != None:
        car.check_right_turn_collision(cars)
    car.check_for_collision(cars)   
    #car.accelerate()
    car.move()
    #car.turn_right()
    root.after(10, drive, car)

# Start the drive function for each car

def change_light_sequence(light1,light2):
    if light1.current_light == "green":
        light1.set_light("yellow")
        light2.set_light("yellow")
        root.after(3000, change_light_sequence,light1,light2)
    elif light1.current_light == "yellow":
        light1.set_light("red")
        light2.set_light("red")
        root.after(9000, change_light_sequence,light1,light2)
    elif light1.current_light == "red":
        light1.set_light("green")
        light2.set_light("green")
        root.after(3000, change_light_sequence,light1,light2)
change_light_sequence(top_left,bottom_right)
#change_light_sequence(top_right,bottom_left)

animate()

for car in cars:
    cars = [car for car in cars if car.active]

    #animate()
    drive(car)


root.mainloop()