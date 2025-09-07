import pygame
import sys

# Initialize Pygame
pygame.init()

# Window size
WINDOW_WIDTH, WINDOW_HEIGHT = 400, 500

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)

class MickeyMouseDrawer:
    def __init__(self):
        # Set up the window
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Mickey Mouse Face")
        self.clock = pygame.time.Clock()
    
    def draw_circle(self, radius, color, x, y):
        # Draw a circle at (x, y)
        pygame.draw.circle(self.screen, color, (int(x), int(y)), int(radius))
    
    def draw_oval(self, width, height, color, rotation, x, y):
        # Create surface with no transparency for solid shapes
        surface = pygame.Surface((width, height))
        surface.fill(color)
        
        # Create mask for oval shape
        mask_surface = pygame.Surface((width, height), pygame.SRCALPHA)
        pygame.draw.ellipse(mask_surface, (255, 255, 255, 255), (0, 0, width, height))
        
        # Apply mask
        surface.set_colorkey((0, 0, 0))  # Make black transparent if needed
        surface = surface.convert()
        
        # For solid ovals, use simple approach
        temp_surface = pygame.Surface((width, height), pygame.SRCALPHA)
        pygame.draw.ellipse(temp_surface, color, (0, 0, width, height))
        
        # Rotate if needed
        if rotation:
            temp_surface = pygame.transform.rotate(temp_surface, rotation)
        
        # Center at (x, y)
        rect = temp_surface.get_rect(center=(int(x), int(y)))
        self.screen.blit(temp_surface, rect)
    
    def mickey_mouse(self):
        # Head BACKGROUND
        self.draw_circle(120, BLACK, WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
        # Ears
        self.draw_circle(70, BLACK, 90, 97)
        self.draw_circle(70, BLACK, 310, 97)

        # Face highlight
        # self.draw_circle(30, YELLOW, WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
        
        # Snout coverup
        self.draw_oval(110, 160, WHITE, 0, 200, 280)
        
        # Cheek outlines
        self.draw_oval(90, 150, WHITE, -220, 250, 296)
        self.draw_oval(90, 150, WHITE, -320, 150, 296)
       
        # Mouth
        self.draw_oval(50, 60, BLACK, 90, 200, 355)
        self.draw_oval(50, 60, WHITE, 90, 200, 350)
        
        # Outer eyes
        self.draw_oval(65, 115, WHITE, 180, 170, 195)
        self.draw_oval(65, 115, WHITE, 180, 235, 195)
        
        # Nose ARCH 
        self.draw_oval(50, 90, BLACK, 90, WINDOW_WIDTH / 2, 270)
        self.draw_oval(50, 95, WHITE , 90, WINDOW_WIDTH / 2, 273)
       
        # NOSE
        self.draw_oval(40, 70, BLACK, 90, WINDOW_WIDTH / 2, 275)
        
        # MOUTH
        self.draw_circle(15, BLACK, 200, 350)
 
        # Eyes
        self.draw_oval(35, 80, BLACK, -175, 180, 209)
        self.draw_oval(35, 80, BLACK, -185, 220, 209)
        self.draw_oval(30, 76, WHITE, -175, 180, 209)
        self.draw_oval(30, 76, WHITE, -185, 220, 209)
        # Pupils
        self.draw_oval(15, 30, BLACK, -175, 185, 233)
        self.draw_oval(15, 30, BLACK, -185, 215, 233)
    
    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (
                    event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
                ):
                    running = False
            
            self.screen.fill(WHITE)
            self.mickey_mouse()
            pygame.display.flip()
            self.clock.tick(60)
        
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    MickeyMouseDrawer().run()