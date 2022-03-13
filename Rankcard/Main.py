# Discord rank card by clarence yang 30/12/21

import requests
from PIL import Image, ImageFont, ImageDraw, ImageOps
from io import BytesIO
from urllib.request import urlopen

class RANKCARD():
    def rank_card(self, username, avatar, level, rank, current_xp, custom_background, xp_color, next_level_xp):

        # create backdrop

        img = Image.new('RGB', (934, 282), color = '#000000')
  
        response = requests.get(avatar) # get avatar picture
        img_avatar = Image.open(BytesIO(response.content)).convert("RGBA")
        

        # create circle mask
        bigsize = (img_avatar.size[0] * 3, img_avatar.size[1] * 3)
        mask = Image.new('L', bigsize, 0)
        draw = ImageDraw.Draw(mask) 
        draw.ellipse((0, 0) + bigsize, fill=255)
        mask = mask.resize(img_avatar.size)
        img_avatar.putalpha(mask)


        img_avatar = img_avatar.resize((170, 170))
        

        img.paste(img_avatar, (50, 50))
        d = ImageDraw.Draw(img)
        d = self.drawProgressBar(d, 260, 180, 575, 40, current_xp/next_level_xp, bg="#484B4E", fg = xp_color) # create progress bar
       


        
        truetype_url = 'https://cdn.fontshare.com/wf/TTX2Z3BF3P6Y5BQT3IV2VNOK6FL22KUT/7QYRJOI3JIMYHGY6CH7SOIFRQLZOLNJ6/KFIAZD4RUMEZIYV6FQ3T3GP5PDBDB6JY.ttf'

        font = ImageFont.truetype(font=urlopen(truetype_url), size=40)
        font2 = ImageFont.truetype(font=urlopen(truetype_url), size=30)
        font3 = ImageFont.truetype(font=urlopen(truetype_url), size=45)
        # add text
        all_xp = f"{current_xp} / {next_level_xp} XP"
        all_level = f"LEVEL {level}"
        w_level, h_level = d.textsize(all_level, font=font)
        w_xp, h_xp = d.textsize(all_xp, font=font2)
        d.text((260, 120),username,(255,255,255), font=font)
        d.text((860 - w_xp, 130),all_xp,(255,255,255), font=font2)
        d.text((860 - w_level, 50),f"LEVEL {level}",xp_color, font=font)
        d.text((260, 45),f"{rank}",(255,255,255), font=font3)


        # save image
        img_border = ImageOps.expand(img,border=25,fill=custom_background)
        return img_border
    
    def drawProgressBar(self, d, x, y, w, h, progress, bg="black", fg="red"):
        # draw background
        d.ellipse((x+w, y, x+h+w, y+h), fill=bg)
        d.ellipse((x, y, x+h, y+h), fill=bg)
        d.rectangle((x+(h/2), y, x+w+(h/2), y+h), fill=bg)

        # draw progress bar
        w *= progress
        d.ellipse((x+w, y, x+h+w, y+h),fill=fg)
        d.ellipse((x, y, x+h, y+h),fill=fg)
        d.rectangle((x+(h/2), y, x+w+(h/2), y+h),fill=fg)

        return d


