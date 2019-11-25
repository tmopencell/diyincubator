# Retrofit an old incubator and run from a web app anywhere in the world

I have come across a lot of old incubators that use old mercury thermometers. In general they are robust and if they still work it is just useful to be able to digitally record and monitor the temperature. 

## 1. Get the incubator
These are usually found left over from universities or from second hand auctions. The ones that use mercury thermometers are ideal from this project as they have a hole already in the top of the housing. 

## 2. Get the computer parts
You  need: 
 - Raspberry pi 3,4 or Zero (or another model is fine as long as you have wifi). 
 - DHT 11 sensor
 - Raspicam
 - A 240V relay
 - An LED display
 - (optional) usb webcamera

 **Where to get them**
If you are in the UK you can be lazy and use this [amazon shopping cart](http://amzn.eu/7rWGZtP) but I find [RS Components](https://uk.rs-online.com) to be the fastest and cheapest (free next day delivery and no minimum order). They stock older raspi versions (3+) which are perfect for this project as well as almost infinite amount of sensors and other electronics. 

## 3. Assemble

I will talk about how I assembled my system but it is likely going to be different for you depending on what type of incubator you found. Hopefully this is useful! My incubator was a B & T UniTemp incubator

## 4. Code to run
This project will require controlling GPIO pins on the Raspberry Pi. The layout of these pins is almost impossible to remember or understand. I recommend this outstanding resource: 
**[Pi GPIO layout](https://pinout.xyz/pinout/pin3_gpio2)**

I will refer exclusively to the actual pin numbers on the device: 1-40

Pin Layout

|   |   |
|---|---|
|   |   |
|   |   |
|   |   |
|   |   |
|   |   |
|   |   |
|   |   |
|   |   |
|   |   |

**Running the Relay**

Using a 5V relay like this requires three pins: 5V, GND, comm (send). 

Pin order

| Relay |  Raspi |
|---|---|
| Vcc |   |
| GND |   |
| Com |   |

**Running the LED display**

Basically just this [blog](https://raspi.tv/2015/how-to-drive-a-7-segment-display-directly-on-raspberry-pi-in-python)

**Creating a timelapse**

**Running the DHT 11**

DHT11 is great because it is a 3 pin device, just like a relay you have a 5V, GND and comm (receive). 

| DHT11  |  Raspi |
|---|---|
| Vcc |   |
| GND |   |
| Com |   |

**Camera and light**

I used a raspicam but you can also use a webcam if you prefer.

```
```

**Record and send to the web**

```

## 5. References and Ideas

Some really cool projects already exist. 

The Pelling lab actually [built an incubator](https://www.pellinglab.net/single-post/diy/DIY-CO2-Incubator-Bioreactor-for-Mammalian-Cell-Culture) from scratch! It is even equiped with CO2 for mamalian cell culture. Really good idea, they just use an old strofoam box as the incubator housing!

A group built an [orbital shaker](https://www.thingiverse.com/thing:2633507) which would fit nicely into an incubator

Dan Chen's Lab have built a quick and easy design for a [single tube mixer](http://danchen.work/lab-shakers/), could be ideal for minipreps.. 



