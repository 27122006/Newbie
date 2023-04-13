import random
def century(year,sex):
    year=int(year)
    century = (year - 1) // 100 + 1
    if century==20 and sex=="male":
        c=0
    elif century==20 and sex=="female":
        c=1
    elif century==21 and sex=="male":
        c=2
    elif century==21 and sex== "female":
        c=3
    elif century==22 and sex== "male":
        c=4
    elif century==22 and sex=="female":
        c=5
    else:
        print("Error gender")
    return c
    
def province(var):
    provinces=["001. Ha Noi", "002. Ha Giang", "004. Cao Bang", 
    "006. Bac Kan", "008. Tuyen Quang", "010. Lao Cai", "011. Dien Bien",
    "012. Lai Chau", "014. Son La", "015. Yen Bai", "017. Hoa Binh",
    "019. Thai Nguyen", "020. Lang Son", "022. Quang Ninh", "024. Bac Giang",
    "025. Phu Tho", "026. Vinh Phuc", "027. Bac Ninh", "030. Hai Duong",
    "031. Hai Phong", "033. Hung Yen", "034. Thai Binh", "035. Ha Nam",
    "036. Nam Dinh", "037. Ninh Binh", "038. Thanh Hoa", "040. Nghe An",
    "042. Ha Tinh", "044. Quang Binh", "045. Quang Tri", "046. Thua Thien Hue",
    "047. Da Nang", "048. Quang Nam", "049. Quang Ngai", "051. Binh Dinh",
    "052. Phu Yen", "053. Khanh Hoa", "054. Ninh Thuan", "058. Binh Thuan",
    "060. Ninh Thuan", "062. Kon Tum", "064. Gia Lai", "066. Dak Lak", 
    "067. Dak Nong", "068.Lam Dong", "070. Binh Phuoc", "072. Tay Ninh", "074. Binh Duong",
    "075. Dong Nai", "077. Ba Ria - Vung Tau", "079. Ho Chi Minh","080.Long An", "082. Tien Giang",
    "083. Ben Tre", "084. Tra Vinh", "086. Vinh Long", "087. Dong Thap", "089. An Giang", "091. Kien Giang", "092. Can Tho",
    "093. Hau Giang", "094. Soc Trang", "095. Bac Lieu", "096. Ca Mau"]
    for p in provinces:
        p_parts = p.split(". ")
        if len(p_parts) == 2 and var == p_parts[1]: # check if the province name matches
            return p_parts[0] # return the number before the province
    return None

def last_two_digit(var):
    return var%100

def random_6():
    number=random.randint(100000,999999)
    return number



