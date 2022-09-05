# UPSliteMAX17040abnormal
All creative credit goes to linshuqin329,
https://github.com/linshuqin329/UPS-Lite/blob/master/UPS_Lite.py

I slightly modified UPSlite.py script for my own upslite v1.2 which does not advertise on default i2c address.
I purchased a "UPSlite v1.2" board from aliexpress. it doesn't communicate on the default i2c address like the seller stated. This is an adaptation of the official py script for my own needs. You may use it as you please if it helps.

I am using it on a bananapi m2 zero. it prints to terminal fine, but I wanted it to a file I can show the contents of on a web dash I'm working on.
You can change file.write() calls to print() and restore that functionality if needed/wanted.
rPI.GPIO seems like it no longer works at all on non rPI boards, so if you need that you should substitute in gpiod.
