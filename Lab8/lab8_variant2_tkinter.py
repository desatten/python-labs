# Лабораторная работа №8. GUI, модуль Tkinter. Вариант 2.
# y(x) = sum((-1)^n*x^n/n!) = e^(-x), z(x) = e^(-x) + b.
import tkinter as tk
from tkinter import messagebox
import math

class GraphApp:
    def __init__(self, root):
        self.root=root; root.title('Лабораторная работа №8 — вариант 2')
        root.geometry('1000x720'); root.minsize(650,480)
        controls=tk.Frame(root,padx=8,pady=8); controls.pack(fill='x')
        self.entries={}
        defaults={'X начальное':'-2','X конечное':'4','Шаг dx':'0.05','Точность ε':'0.000001','Смещение b':'1'}
        for label,value in defaults.items():
            tk.Label(controls,text=label+':').pack(side='left',padx=(5,2))
            entry=tk.Entry(controls,width=9); entry.insert(0,value); entry.pack(side='left',padx=2)
            self.entries[label]=entry
        tk.Button(controls,text='Построить графики',command=self.draw).pack(side='left',padx=8)
        self.canvas=tk.Canvas(root,bg='white',highlightthickness=0); self.canvas.pack(fill='both',expand=True,padx=8,pady=8)
        self.status=tk.Label(root,text='Синий — сумма ряда Тейлора; красный — e^(-x)+b.',anchor='w'); self.status.pack(fill='x',padx=10,pady=(0,8))
        self.canvas.bind('<Configure>',lambda event:self.draw())
    def taylor_exp_minus_x(self,x,eps):
        term=1.0; total=term; n=1
        while n<10000:
            term *= -x/n; total += term
            if abs(term)<eps: return total,n
            n+=1
        raise ValueError('Ряд не достиг заданной точности за 10000 членов.')
    def draw(self):
        try:
            a=float(self.entries['X начальное'].get()); z=float(self.entries['X конечное'].get())
            dx=float(self.entries['Шаг dx'].get()); eps=float(self.entries['Точность ε'].get()); b=float(self.entries['Смещение b'].get())
            if not all(map(math.isfinite,(a,z,dx,eps,b))) or a>=z or dx<=0 or eps<=0: raise ValueError('Требуется Xнач < Xкон, dx > 0, ε > 0 и конечные числа.')
            if (z-a)/dx>20000: raise ValueError('Слишком много точек: уменьшите диапазон или увеличьте dx.')
            xs=[]; ys=[]; zs=[]; x=a
            while x<=z+dx*1e-9:
                y,_=self.taylor_exp_minus_x(x,eps); xs.append(x); ys.append(y); zs.append(math.exp(-x)+b); x+=dx
            self.canvas.delete('all'); w=max(100,self.canvas.winfo_width()); h=max(100,self.canvas.winfo_height())
            ymin=min(ys+zs); ymax=max(ys+zs); pad=max((ymax-ymin)*0.1,0.1); ymin-=pad; ymax+=pad
            left,right,top,bottom=65,w-25,25,h-55
            px=lambda x:left+(x-a)/(z-a)*(right-left)
            py=lambda y:bottom-(y-ymin)/(ymax-ymin)*(bottom-top)
            # Сетка и оси с подписями.
            for i in range(6):
                yy=ymin+i*(ymax-ymin)/5; Y=py(yy)
                self.canvas.create_line(left,Y,right,Y,fill='#e5e5e5')
                self.canvas.create_text(left-8,Y,text=f'{yy:.3g}',anchor='e')
            self.canvas.create_line(left,bottom,right,bottom,fill='black',width=2)
            self.canvas.create_line(left,top,left,bottom,fill='black',width=2)
            for i in range(6):
                xx=a+i*(z-a)/5; X=px(xx)
                self.canvas.create_line(X,bottom,X,bottom+4,fill='black')
                self.canvas.create_text(X,bottom+17,text=f'{xx:.3g}')
            self.canvas.create_text((left+right)/2,h-15,text='x')
            self.canvas.create_text(15,(top+bottom)/2,text='y',angle=90)
            def plot(values,color):
                coords=[]
                for xx,yy in zip(xs,values): coords.extend((px(xx),py(yy)))
                if len(coords)>=4: self.canvas.create_line(*coords,fill=color,width=2,smooth=True)
            plot(ys,'#1565c0'); plot(zs,'#d32f2f')
            self.canvas.create_text(left+10,top+8,text='y(x) — ряд Тейлора',fill='#1565c0',anchor='nw')
            self.canvas.create_text(left+10,top+27,text=f'z(x) = e⁻ˣ + b, b = {b:g}',fill='#d32f2f',anchor='nw')
            self.status.config(text=f'Построено точек: {len(xs)}. Диапазон Y: [{min(ys+zs):.5g}; {max(ys+zs):.5g}].')
        except (ValueError,OverflowError) as exc:
            self.canvas.delete('all'); self.status.config(text='Ошибка исходных данных.')
            messagebox.showerror('Ошибка ввода',str(exc))

if __name__=='__main__':
    root=tk.Tk(); app=GraphApp(root); root.after(100,app.draw); root.mainloop()
