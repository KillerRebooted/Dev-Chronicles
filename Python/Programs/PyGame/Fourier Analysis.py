import math
import cmath
import pygame as pg


# ============================================================
# 1. INTERPOLATION
# ============================================================

def interpolate(z, depth):
    """
    Smoothens the input path by inserting midpoints
    between consecutive complex coordinates.

    depth determines how many times interpolation
    is repeated. Each iteration increases the number
    of points and produces a smoother path.
    """

    for _ in range(depth):

        interpolated_z = []
        
        for i in range(len(z)):

            # Select the next point, wrapping around
            # to the first point at the end of the list.
            j = i + 1

            if i == len(z) - 1:
                j = 0

            p1 = z[i]
            p2 = z[j]

            # Insert the original points and their midpoint.
            interpolated_z.extend([
                p1,
                (p1 + p2) / 2,
                p2
            ])

        z = interpolated_z

    # Reverse the sequence before returning it.
    return interpolated_z[::-1]


# ============================================================
# 2. DISCRETE FOURIER TRANSFORM
# ============================================================

def fourier(z):
    """
    Calculates the Discrete Fourier Transform (DFT)
    of the input complex-coordinate path.

    Each Fourier coefficient represents an epicycle.

    Ck determines:
    - The radius of the epicycle: abs(Ck)
    - Its initial phase: arg(Ck)

    k determines its rotational frequency.
    """

    N = len(z)

    C = []

    # Calculate Fourier coefficients for each frequency.
    for k in range(-N//2, N//2 + 1):

        summation = 0

        for n in range(0, N-1+1):

            # DFT formula:
            # Ck = (1/N) * sum(z[n] * exp(-i*2*pi*k*n/N))

            summation += z[n] * cmath.exp(
                -1j * ((2 * cmath.pi * k * n) / N)
            )

        Ck = summation / N

        C.append((k, Ck))

    # Sort epicycles by amplitude.
    # Larger circles are placed first, followed by smaller ones.

    C.sort(
        key=lambda item: cmath.polar(item[1])[0],
        reverse=True
    )

    return C


# ============================================================
# 3. FOURIER EPICYCLE VISUALIZATION
# ============================================================

def main(z, speed):
    """
    Animates the Fourier reconstruction of the input path.

    Each Fourier coefficient is visualized as a rotating
    circle (epicycle).

    The endpoint of the final epicycle traces the
    reconstructed shape over time.
    """

    pg.init()

    # Initialize display dimensions.
    width, height = 800, 600

    screen = pg.display.set_mode((width, height))

    pg.display.set_caption("Fourier Epicycles")

    clock = pg.time.Clock()

    # Running time variable.
    time = 0.0

    # Calculate Fourier coefficients.
    C = fourier(z)

    # Stores the trajectory traced by the epicycle endpoint.
    path = []

    # Main application loop.
    running = True

    while running:

        # ----------------------------------------------------
        # EVENT HANDLING
        # ----------------------------------------------------

        for event in pg.event.get():

            if event.type == pg.QUIT:
                running = False

            # Left mouse click activates manual drawing mode.
            elif event.type == pg.MOUSEBUTTONDOWN:

                if event.button == 1:

                    running = "drawing"

                    z = []
                    path = []

        # Calculate elapsed time in seconds.
        dt = clock.tick(240) / 1000.0

        # Clear the screen.
        screen.fill((0, 0, 0))

        # ====================================================
        # 4. MANUAL DRAWING MODE
        # ====================================================

        if running == "drawing":

            # Check whether the left mouse button is held.
            mouse_buttons = pg.mouse.get_pressed()

            MIN_DISTANCE = 1

            if mouse_buttons[0]:

                mouse_pos = pg.mouse.get_pos()

                # Only record points sufficiently far apart
                # to avoid excessive duplicate coordinates.

                if (
                    not path
                    or math.dist(mouse_pos, path[-1]) > MIN_DISTANCE
                ):

                    # Convert screen coordinates into complex
                    # coordinates centered around the origin.

                    z.append(
                        complex(
                            (mouse_pos[0] - width/2) / 200,
                            (mouse_pos[1] - height/2) / 200
                        )
                    )

                    path.append(mouse_pos)

                    # Display the path while drawing.
                    if len(z) > 1:

                        pg.draw.aalines(
                            screen,
                            (0, 255, 255),
                            False,
                            path
                        )

            else:

                # When drawing ends, calculate the Fourier series.
                running = True

                C = fourier(z)

                path = []
                time = 0.0

            pg.display.flip()

        # ====================================================
        # 5. FOURIER RECONSTRUCTION MODE
        # ====================================================

        else:

            # Advance time.
            # Multiplying dt by 'speed' controls animation speed.

            time += dt * speed

            screen.fill((0, 0, 0))

            # ------------------------------------------------
            # DISPLAY ORIGINAL INPUT SHAPE
            # ------------------------------------------------

            screen_points = []

            for point in z:

                x = int(point.real * 200 + width / 2)

                y = int(point.imag * 200 + height / 2)

                screen_points.append((x, y))

            # Connect the original coordinates to display
            # the reference shape.

            if len(screen_points) > 1:

                pg.draw.aalines(
                    screen,
                    (0, 255, 255),
                    True,
                    screen_points
                )

            # ------------------------------------------------
            # DRAW THE EPICYCLE CHAIN
            # ------------------------------------------------

            # All epicycles originate from the center of
            # the screen. Each subsequent epicycle begins
            # at the endpoint of the previous one.

            center = (width / 2, height / 2)

            for k, Ck in C:

                # Polar representation of Fourier coefficient.
                # Magnitude gives radius; phase gives initial angle.

                radius = cmath.polar(Ck)[0] * 200

                initial_phase = cmath.polar(Ck)[1]

                # Angular position at the current time.
                # k determines the rotational frequency.

                theta = initial_phase + (k * time)

                # Draw the circular epicycle.
                pg.draw.circle(
                    screen,
                    (255, 255, 255),
                    center,
                    radius,
                    width=1
                )

                # Calculate the endpoint of this epicycle.
                next_center = (
                    center[0] + radius * math.cos(theta),
                    center[1] + radius * math.sin(theta)
                )

                # Draw the rotating radius.
                pg.draw.line(
                    screen,
                    (255, 0, 0),
                    center,
                    next_center,
                    width=1
                )

                # The next epicycle starts where this one ends.
                center = next_center

            # ------------------------------------------------
            # DRAW THE RECONSTRUCTED PATH
            # ------------------------------------------------

            # Store the endpoint of the final epicycle.
            path.append(center)

            # Connect successive endpoints to reveal
            # the reconstructed Fourier drawing.

            if len(path) > 1:

                pg.draw.aalines(
                    screen,
                    (255, 0, 255),
                    False,
                    path
                )

            # Refresh the display.
            pg.display.flip()

    # Close Pygame.
    pg.quit()


# ============================================================
# 6. PROGRAM ENTRY POINT
# ============================================================

if __name__ == "__main__":

    # Example: Square centered at the origin.
    # Its four vertices are represented as complex numbers.

    z = [
        1 + 1j,
        1 - 1j,
        -1 - 1j,
        -1 + 1j
    ]

    # Increase the number of points through interpolation.
    z = interpolate(z, 5)

    # Start Fourier epicycle visualization.
    main(z, speed=1.5)
