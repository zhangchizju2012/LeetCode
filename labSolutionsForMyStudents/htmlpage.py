

def main():
  inp = open("input.txt", 'r')
  
  marks = []
  
  for line in inp.readlines():
    parts = line.split(" ")
    marks.append(int(parts[1]))
  
  avg = 0
  min = 101
  max = -1
  size = 0
  
  for m in marks:
    if m < min:
      min = m
    if m > max:
      max = m
    avg += m
    size += 1
    
  avg /= size
  
  tags = "<html> <body> <h1> <b> Welcome to statistics page! </b> </h1> "
  
  html = "<br/> Average is: " + str(avg) + "<br/>Minimum is: " + str(min) + "<br/>Maximum is: " + str(max) + "<br/><br/><br/>"
  
  bars = []
  
  for i in range(0,10):
    bars.append(0)
    
  for m in marks:
    bars[m//10] += 1
  
  chart = "<table> <tr> "
  line2 = "<tr>"
  
  i=0
  for b in bars:
    height = 20 * b
    chart += "<td valign=\"bottom\"> <div style=\"width:30px;height:" + str(height) + "px;background:blue;border:1px solid red;\"> </div></td>"
    line2 += "<td style=\"width:50px;\"> [" + str(i) + "-" + str(i+9) + "] </td>"
    i += 10
  
  chart += "</tr>"
  endtags = " </tr> </table> </body></html>"
  
  out = open("output.html", 'w')
  out.write(tags + html + chart + line2 + endtags)

main()