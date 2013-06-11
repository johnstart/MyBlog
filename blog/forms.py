# # -*- coding: cp936 -*-
# __author__ = 'QJL'
#
# from django import forms
# from tinymce.widgets import TinyMCE
#
# from captcha.fields import CaptchaField
#
# class ContactForm(forms.Form):
#     subject=forms.CharField()
#     e_mail=forms.EmailField(required=False)
#     message=forms.CharField(widget=forms.Textarea)
#
# class PictureForm(forms.Form):
#     imageFile=forms.ImageField()
#
#
# class addComment(forms.Form):
#     name=forms.CharField(label=u"昵称")
#     e_mail=forms.EmailField(label=u"邮箱")
#     content=forms.CharField(label=u"内容", widget = TinyMCE() )
#     captcha=CaptchaField(label=u"验证码")
#     #添加自定义的表单验证
#     def clean_content(self):
#         content=self.cleaned_data['content']
#         num_words=len(content.split())
#         if num_words<4:
#             raise forms.ValidationError(u"输入内容不够!")
#         return content
#
#
