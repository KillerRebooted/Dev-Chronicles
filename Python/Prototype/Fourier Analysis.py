import math
import cmath
import pygame as pg

def interpolate(z, depth):

    for _ in range(depth):

        interpolated_z = []
        
        for i in range(len(z)):
            j = i+1
            if i == len(z)-1:
                j = 0

            p1 = z[i]
            p2 = z[j]
            interpolated_z.extend([p1, (p1+p2)/2, p2])

        z = interpolated_z

    return interpolated_z[::-1]

def fourier(z):
    
    N = len(z)

    C = []
    for k in range(-N//2, N//2 + 1):
        summation = 0
        for n in range(0, N-1+1):
            summation += z[n] * cmath.exp(-1j * ((2*cmath.pi*k*n)/N))
        Ck = summation/N
        C.append((k, Ck))

    C.sort(key=lambda item: cmath.polar(item[1])[0], reverse=True)

    return C

def main(z):
    pg.init()

    width, height = 800, 600
    screen = pg.display.set_mode((width, height))
    pg.display.set_caption("Fourier Epicycles")

    clock = pg.time.Clock()
    time = 0.0  # Our running time variable

    C = fourier(z)

    path = []
    # Main loop
    running = True
    while running:
        # Event handling (detecting if the user closes the window)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        dt = clock.tick(60) / 1000.0  # Converts ms to seconds
    
        # Advance time (you can multiply by a speed factor if you want it faster/slower)
        time += dt * 2

        # Clear screen with black
        screen.fill((0, 0, 0))

        screen_points = []
        for point in z:
            x = int(point.real * 200 + width / 2)
            y = int(point.imag * 200 + height / 2)  # Pygame Y goes down, so you can flip if needed with -point.imag
            screen_points.append((x, y))

        # Draw the shape lines connecting the points (True means close the loop)
        if len(screen_points) > 1:
            pg.draw.aalines(screen, (0, 255, 255), True, screen_points)

        center = (width/2, height/2)
        for k, Ck in C:
            radius = cmath.polar(Ck)[0]*200
            initial_phase = cmath.polar(Ck)[1]

            theta = initial_phase + (k*time)
            
            pg.draw.circle(screen, (255, 255, 255), center, radius, width=3)
            next_center = (center[0] + radius*math.cos(theta), center[1] + radius*math.sin(theta))
            pg.draw.line(screen, (255, 0, 0), center, next_center, width=3)
            center = next_center

        path.append(center)

        if len(path) > 1:
            pg.draw.aalines(screen, (255, 0, 255), False, path)
        
        # Refresh the display frame
        pg.display.flip()

    pg.quit()

if __name__ == "__main__":
    
    z = [
    1.0 + 0.0j,
    0.4 + 0.7j,
    -0.2 + 1.3j,
    -0.8 + 0.5j,
    -1.4 - 0.2j,
    -0.7 - 1.1j,
    0.1 - 1.5j,
    0.7 - 0.8j,
    1.3 - 0.3j
    ]

    z = interpolate(z, 5)

    main(z)