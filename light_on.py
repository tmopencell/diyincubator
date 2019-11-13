import RPi.GPIO as GPIO
GPIO.setwarnings(False)
# Set pin numbering can use BOARD or BCM
GPIO.setmode(GPIO.BCM)

# Pick your pins
#GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(16, GPIO.OUT, initial=GPIO.LOW)
# Turn the pin on by setting it HIGH:
GPIO.output(16,GPIO.HIGH)
# Or if you want to turn it off set it LOW:
# GPIO.output(2,GPIO.LOW)
