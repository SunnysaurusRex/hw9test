#!/usr/local/bin/python
import cgi
import cgitb
cgitb.enable()
print( "Content-type: text/html\n\n" )
print( "<html><body>" )
form = cgi.FieldStorage()

if "A" in form:
 print("""
  <html>
  <head>
   <title>hw9 chart.py</title>
   <script src="hw9.js" type="text/javascript"></script>
   <link rel="stylesheet" href="hw9.css" type="text/css" />
  </head>
  </html>
   <h1>SunHung Zhao</h1>
   <h1>CS102D</h1>
   <h1>November 7 2018</h1>
   <h1>Homework-9</h1>
   <h1>chart.py</h1>
   <button type="button" onClick=reveal()>Click to reveal table</button>
""")

 print("<table class=invisible id=recta>")
 print("<tr> <th>x</th> <th>y</th> <th>dy</th> <th>integral-y</th> </tr>")

 h = 5
 def function( z ):
        return int(form["A"].value)*z - int(form["B"].value)*z*z*z + int(form["C"].value)*z*z*z
 def fp( x ):
        return ( function(x + h) - function( x ) ) / h
 def fin( x ):
        return ( ( function( x ) + fp( x ) ) / 2 ) * h
 def fpp( x ):
        return ( fp(x + h) - fp( x ) ) / h
 x = -100
 yint = 0
 while x <=100:
   y = function( x )
   yp = fp( x )
   yin = fin( x )
   yint = yint + yin
   yaccel = fpp( x )
   if x%2 == 0: print("<tr class=even> <td>%d</td> <td>%d</td> <td>%d</td> <td>%d</td> </tr>" $
   else: print("<tr class=odd> <td>%d</td> <td>%d</td> <td>%d</td> <td>%d</td> </tr>" %(x,y,yp$

   x = x + 1
print("</table>")


print( "</body></html>" )


