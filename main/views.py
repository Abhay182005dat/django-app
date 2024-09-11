from django.shortcuts import render

# Create your views here.
def add_numbers(request):
    result = None
    error = None

    if request.method == "POST":
        num1 = request.POST.get('num1')
        num2 = request.POST.get('num2')

        try:
          sum = float(num1) + float(num2)
          result = f"The sum is: {sum}"
        except:
           error = "Something went wrong"
    return render(request, 'add.html' , {'result':result , 'error':error})

def pnr(request):
   
  result  = None
  error = None

  if request.method == "POST":
      num1 = request.POST.get('num1')
      num2 = request.POST.get('num2')
      num3 = request.POST.get('num3')

      try:
         si = (float(num1)*float(num2)*float(num3)) / 100
         result = f"The Simple Interest is {si}"
      except:
          error = "Something went wrong"
  return render(request, 'pnr.html' , {'result':result , 'error':error})
