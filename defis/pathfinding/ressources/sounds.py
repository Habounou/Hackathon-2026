import pygame
import sys
import math
import numpy as np


def checkQuit():
    """Checks if the user wants to close the application.
    
    Monitors pygame events for quit signals and handles application
    shutdown gracefully if a quit event is detected.
    """
    try:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    except:
        pass


def beep(duration: float, frequency: int):
    """Plays a beep sound with specified duration and frequency.
    
    How it works:
    1. We need to create a list of numbers representing the sound wave
    2. Each number is a "sample" - a point on the wave
    3. We use sin() to create a smooth wave at the right frequency
    4. pygame turns this list into actual sound
    
    Args:
        duration (float): Duration of the beep in seconds.
        frequency (int): Frequency of the beep in hertz.
    """
    # Step 1: Initialize sound system
    if not pygame.mixer.get_init():
        pygame.mixer.init(frequency=22050, size=-16, channels=2)
    
    # Step 2: Figure out how many samples we need
    sample_rate = 22050  # samples per second
    num_samples = int(duration * sample_rate)  # total samples needed
    
    # Step 3: Create the wave - just a list of numbers
    wave = []
    for i in range(num_samples):
        # sin() creates the wave shape
        # 2*pi*frequency is how fast it oscillates
        # i/sample_rate is the current time in seconds
        angle = 2 * math.pi * frequency * i / sample_rate
        sample_value = int(8000 * math.sin(angle))
        
        # Stereo: [left_speaker, right_speaker]
        wave.append([sample_value, sample_value])
    
    # Convert to numpy array (pygame needs this format)
    wave = np.array(wave, dtype=np.int16)
    
    # Step 4: Turn the array into sound and play it
    sound = pygame.sndarray.make_sound(wave)
    sound.play()
    pygame.time.wait(int(duration * 1000))
    
    checkQuit()


def sleep(time: float):
    """Pauses execution for a specified duration in seconds.
    
    Args:
        time (float): Duration in seconds.
    """
    pygame.time.delay(int(time * 1000))
    checkQuit()
    
    
def winSound():
    """Plays a victory sound with ascending tones followed by celebration beeps.
    
    Creates an upward sweep from 500Hz to 1000Hz, followed by three
    celebratory beeps at 1000Hz with the final beep sustained longer.
    """
    for frequence in range(500, 1000 + 1, 100):
        beep(0.1, frequence)
    sleep(0.8)
    for fois in range(3):
        beep(0.1 + 0.3 * (fois == 2), 1000)
        sleep(0.2)


def loseSound():
    """Plays a defeat sound with descending tones.
    
    Creates a downward sweep from 1000Hz to 500Hz to indicate failure.
    """
    for frequence in range(1000, 500 - 1, -100):
        beep(0.1, frequence)


def teleportSound():
    """Plays a teleportation sound effect with quick frequency changes.
    
    Creates a sci-fi teleport effect with descending-then-ascending tones.
    """
    beep(0.05, 800)
    beep(0.05, 600)
    beep(0.1, 1200)


def refuelSound():
    """Plays a refueling sound with ascending tones.
    
    Creates a power-up effect with three quick ascending beeps.
    """
    beep(0.08, 400)
    beep(0.08, 600)
    beep(0.08, 800)

def checkpointSound():
    """Plays a checkpoint sound.
    
    Short confirmation tone pair to indicate a checkpoint was collected.
    """
    beep(0.06, 700)
    beep(0.08, 900)

def waterSound():
    """Short water splash-like chirp."""
    beep(0.03, 900)
    beep(0.03, 700)

def mudSound():
    """Short low rumble for mud."""
    beep(0.06, 300)