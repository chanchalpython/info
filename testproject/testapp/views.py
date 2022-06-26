from django.shortcuts import render
from .forms import MasterForm


# Create your views here.
def home(request):
    context={}
    context['form'] = MasterForm()

    if request.method == 'POST':
        form = MasterForm(request.POST)
        if form.is_valid():
            masterstr = form.cleaned_data['masterstr']
            str1 = form.cleaned_data['str1']
            str2 = form.cleaned_data['str2']
            str3 = form.cleaned_data['str3']
            str4 = form.cleaned_data['str4']


         # if form.is_valid():

            # for let in master:
            #     letters.append(let)
            # for val1 in str1:
            #     string1.append(val1)
            # for val2 in str2:
            #     string2.append(val2)
            # for val3 in str3:
            #     string3.append(val3)
            # for val4 in str4:
            #     string4.append(val4)
            # if string1 in letters:
            #     print('ok')
            masterstr="aabcglactdde"
            strs={'cat':str1,'egg':str2,'ball':str3,'bat':str4}
            print(strs)
            print(masterstr)
            for strs in masterstr:
                print("yes")
            else:
                print("NO")
        #     if strs in materstr:
        #      print("yes")
        #     strs.pop(masterstr)
        # else:
        #     print("NO")



    return render(request, "home.html", context)
