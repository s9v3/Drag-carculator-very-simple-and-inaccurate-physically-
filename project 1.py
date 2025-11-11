p_liquid=float(input("유체의 밀도(kg*m^3)를 입력해 주세요: "))
L_liquid=float(input("유동의 특성길이(M)를 입력해 주세요: "))
u_liquid=float(input("유체의 점성계수를 입력해 주세요: "))
A=float(input("물체의 전면 참조 영역(m^2)을 입력해 주세요: "))
V=float(input("물체의 속력(m/s)값을 입력해 주세요: "))
object=input("물체의 형상을 입력하세요('sphere,'plate','wing' 중 택1): ")
object_feature=input("물체의 표면을 입력하세요('smooth', 'rough'중 택1): ")

def sphere_smooth(re):
    if re<=10**3:
        drag_coefficient_sphere_smooth=(24/re)+4/(re**(1/3))
    elif re>10**3 and re<=10**(5.48):
        drag_coefficient_sphere_smooth=0.45
    elif re>10**(5.48) and re<=10**(5.82):
        drag_coefficient_sphere_smooth=0.08
    else:
        drag_coefficient_sphere_smooth=re*(10*(-7))
    return drag_coefficient_sphere_smooth

def sphere_rough(re):
    if re<=10**3:
        drag_coefficient_sphere_rough=(24/re)+4/(re**(1/3))
    elif re>10**3 and re<=10**(4.89):
        drag_coefficient_sphere_rough=0.45
    elif re>10**(4.89) and re<=10**(5.28):
        drag_coefficient_sphere_rough=0.31
    else:
        drag_coefficient_sphere_rough=re*(10*(-7))
    return drag_coefficient_sphere_rough

def plate(re):
    return 1.5

def Airfoil(re):
    if re<=10**(5.27):
        drag_coefficient_airfoil=(0.1-(re/(10**(re+1))))
    elif re>10**(5.27) and re<=10**(6.38):
        drag_coefficient_airfoil=0.02
    else:
        drag_coefficient_airfoil=0.01
    return drag_coefficient_airfoil

def Drag(Cd, p, A, V):
    return (1/2)*Cd*p*A*(V**2)

if object=='sphere' and object_feature=='smooth':
    for i in range(1, int(V) + 1, 1):
        Re = (p_liquid * i * L_liquid) / u_liquid
        result=Drag(sphere_smooth(Re), p_liquid, A, i)
        print(f"속력이 {i}m/s일 때 {object_feature} {object}의 구조항력은 {(result)}입니다.")
elif object=='sphere' and object_feature=='rough':
    for i in range(1, int(V) + 1, 1):
        Re = (p_liquid * i * L_liquid) / u_liquid
        result=Drag(sphere_rough(Re), p_liquid, A, i)
        print(f"속력이 {i}m/s일 때 {object_feature} {object}의 구조항력은 {(result)}입니다.")
elif object=='plate':
    for i in range(1, int(V) + 1, 1):
        Re = (p_liquid * i * L_liquid) / u_liquid
        result=Drag(plate(Re), p_liquid, A, i)
        print(f"속력이 {i}m/s일 때 {object}의 구조항력은{(result)}입니다.")
elif object=='wing':
    for i in range(1, int(V) + 1, 1):
        Re = (p_liquid * i * L_liquid) / u_liquid
        result=Drag(Airfoil(Re), p_liquid, A, i)
        print(f"속력이 {i}m/s일 때 {object}의 구조항력은{(result)}입니다.")

