import RPi.GPIO as GPIO
GPIO.setwarnings(False)
# Set pin numbering can use BOARD or BCM
GPIO.setmode(GPIO.BCM)

# Pick your pins
#GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(17, GPIO.OUT, initial=GPIO.HIGH)
#GPIO.setup(27, GPIO.OUT, initial=GPIO.HIGH)
# Turn the pin on by setting it HIGH:
GPIO.output(17,GPIO.HIGH)
#GPIO.output(27,GPIO.HIGH)
print "Sending PINS 17 and 27 HIGH (BCM numbering see https://pinout.xyz/ for more details)"
# Or if you want to turn it off set it LOW:
# GPIO.output(2,GPIO.LOW)
