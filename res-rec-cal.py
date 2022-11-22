from math import sqrt

def main():
    veriler = take_circle_inputs()
    
    intersecting_list, non_intersecting_list = create_circle_lists(veriler)

    area = 0
    for i in non_intersecting_list:
        area += i.compute_singular_bound_area()
    for i in intersecting_list:
        area += i.compute_total_bound_area()
    
    for i in veriler:
        print("(", i.x, i.y, ") rad:", i.r)
    print("Total rect area:", area)
        
    
class Circle:
    def __init__(self,x,y,r):
        self.x = x
        self.y = y
        self.r = r
    
    def max_x(self):
            return int((self.x)+(self.r))
        
    def min_x(self):
            return int((self.x)-(self.r))
        
    def max_y(self):
            return int((self.y)+(self.r))
        
    def min_y(self):
            return int((self.y)-(self.r))
    
    def compute_singular_bound_area(self):
        return ((2 * (self.r)) ** 2)

class Intersecting_Circles:
    def __init__(self,circle_one,circle_two):
        self.circle_one = circle_one
        self.circle_two = circle_two
    
    def compute_total_bound_area(self):
        maximum_x = 0
        minimum_x = 0
        maximum_y = 0
        minimum_y = 0

        if self.circle_one.max_x() > self.circle_two.max_x():
            maximum_x = self.circle_one.max_x()
        else:
            maximum_x = self.circle_two.max_x()
        if self.circle_one.min_x() < self.circle_two.min_x():
            minimum_x = self.circle_one.min_x()
        else:
            minimum_x = self.circle_two.min_x()
        if self.circle_one.max_y() > self.circle_two.max_y():
            maximum_y = self.circle_one.max_y()
        else:
            maximum_y = self.circle_two.max_y()
        if self.circle_one.min_y() < self.circle_two.min_y():
            minimum_y = self.circle_one.min_y()
        else:
            minimum_y = self.circle_two.min_y()
        
        area = abs(maximum_x - minimum_x) * abs(maximum_y - minimum_y)
        return int(area)

def take_circle_inputs():
    cember_sayisi = int(input())
    dondur = list()
    for i in range(0,cember_sayisi):
        cember_verisi = input().split(" ")
        dondur.append(Circle(int(cember_verisi[0]), int(cember_verisi[1]), int(cember_verisi[2])))
    return dondur

def check_if_intersect(cember_bir, cember_iki):
    distance_of_x = abs(cember_bir.x - cember_iki.x)
    distance_of_y = abs(cember_bir.y - cember_iki.y)
    distance_of_centers = sqrt(((distance_of_x ** 2) + (distance_of_y ** 2)))
    kontrol_uzunlugu = cember_bir.r + cember_iki.r
    return (kontrol_uzunlugu > distance_of_centers)

def create_circle_lists(liste):
    non_intersecting_circles = list()
    intersecting_circles = list()
    inter_circles_for_checking = list()
    for cember_bir in liste:
        if cember_bir != liste[-1]:
            for cember_iki in liste[liste.index(cember_bir)+1:]:
                if check_if_intersect(cember_bir, cember_iki):
                    intersecting_circles.append(Intersecting_Circles(cember_bir, cember_iki))
    for i in intersecting_circles:
        inter_circles_for_checking.append(i.circle_one)
        inter_circles_for_checking.append(i.circle_two)
    for i in liste:
        if i not in inter_circles_for_checking:
            non_intersecting_circles.append(i)
    return intersecting_circles, non_intersecting_circles
main()