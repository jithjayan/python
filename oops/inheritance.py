# class syn():
#     def python(self):
#         self.a=10
#         print("python")
#     def php(self):
#         print("php")

# class novavi(syn):
#     def dm(self):
#         print("dm works")
#     def web_dev(self):
#         print("web dev")

# novavi_staff=novavi()
# novavi_staff.python()
# novavi_staff.php()
# print(novavi_staff.a)

# std1=syn()
# std1.python()


# class father:
#     def shop(self):
#         print("hotel")
#     def car(self):
#         print("polo gt")
# class mother:
#     def dress_shop(self):
#         print("dress shop")
# class child(father,mother):
#     def bike(self):
#         print("bike")
# sonu=child()
# sonu.shop()
# sonu.car(),sonu.dress_shop()


# class school:
#     def notes(self):
#         print("lecture notes")
#     def online(self):
#         print("online classes")

# class tution:
#     def tu_notes(self):
#         print("tuition notes")
#     def gu_notes(self):
#         print("guide notes")

# class student(school,tution):
#     def text_notes(self):
#         print("text refered notes")
# harley=student()
# harley.notes()
# harley.online()
# harley.tu_notes()

# class KU:
#     def exam(self):
#         print("exam")
#     def result(self):
#         print("result")

# class clg:
#     def notes(self):
#         print("lecture notes")
# class std(KU,clg):
#     def uniform(self):
#         print("uniform")
# harley=std()
# harley.exam()
# harley.result()
# harley.notes()  

# class syn:
#     def python(self):
#         print('python')
#     def php(self):
#         print('php')
# class nonteaching_staff(syn):
#     def admission(self):
#         print('adm')
# class teaching_staff(syn):
#     def python_cor(self):
#         print('python cor')
# staff1=nonteaching_staff()
# staff2=teaching_staff()
# staff1.python()
# staff1.admission()5
# staff2.python_cor()   

# class syn:
#     def python(self):
#         print('python')
#     def php(self):
#         print('php')
# class nonteaching_staff(syn):
#     def admission(self):
#         print('adm')
# class teaching_staff(syn):
#     def python_cor(self):
#         print('python cor')
# class std(teaching_staff):
#     def notes(self):
#         print('notes')
# staff1=nonteaching_staff()
# staff2=teaching_staff()
# std1=std()
# staff1.python()
# staff2.python_cor()
# std1.notes()

class lib:
    def reading(self):
        print('readings')
class admin(lib):
    def adm(self):
        print('adm')
class book(admin):
    def novel(self):
        print('novel')
    def comic(self):
        print('comic')
class newspaper(admin):
    def news(self):
        print('news')
class user(book,newspaper):
    def user(self):
        print('user')
user1=user()
user1.reading()


