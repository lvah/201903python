"""
表单文件
"""

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, SelectMultipleField
from wtforms.validators import DataRequired, Length, Email, EqualTo, Regexp, ValidationError


class LoginForm(FlaskForm):
    email = StringField(label="电子邮箱",
                        validators=[
                            DataRequired(message='邮箱不能为空'),
                            Length(1, 15, message="长度不符合条件"),
                            Email(message='请输入有效的邮箱地址,比如:username@domain.com')
                        ])
    password = PasswordField('密码',
                             validators=[
                                 DataRequired(message=u'密码不能为空')])
    submit = SubmitField(u'登录')

class RegisterForm(FlaskForm):
    # StringField <input type='text' name='name' required>
    # PasswordField <input type='password' name='password' required>
    name = StringField(
        label="用户名",
        # 验证: 用户名不能为空的
        validators=[DataRequired(message='用户名不能为空'),Length(5, 12, message="用户名长度必须在5-12之间") ]
    )
    password = PasswordField(
        label="密码",
        validators=[
            DataRequired(),
            # 验证密码长度是否为6～8之间， 如果不是， 则报错;
            Length(6, 16, message="密码格式不正确"),
        ]
    )
    repassword = PasswordField(
        "确认密码",
        validators=[
            DataRequired(),
            # 验证当前表单输入的内容和password这个表单输入的内容是否一致， 如果不一致， 报错;
            EqualTo('password', message="密码不一致")

        ]
    )

    # email = StringField(
    #     label="邮箱",
    #     validators=[
    #         DataRequired(),
    #         # 验证当前表单输入的内容是否为一个邮箱地址， 如果不是， 则报错;
    #         Email(message="邮箱格式错误!")
    #
    #     ]
    # )
    # phone = StringField(
    #     label="电话号码",
    #     validators=[
    #         DataRequired(),
    #         # 验证当前表单输入的电话号码是否符合首位为1，由11位数字组成的正则表达式， 如果不是， 则报错;
    #         Regexp(r'1\d{10}', message="电话号码格式错误!")
    #     ]
    # )
    #
    #
    # # 可以实现单选按钮， 但是不美观，
    # # gender = RadioField(
    # #     label="性别",
    # #     coerce=int,
    # #     choices=[(1, "男"), (2, "女")]
    # #
    # # )
    #
    # # 下拉单选框
    # gender = SelectField(
    #         label="性别",
    #         # 填写的信息传入后台的类型;
    #         coerce=int,
    #         # 下拉列表的选项
    #         choices=[(1, "男"), (2, "女")]
    # )
    #
    # # 下拉多选框
    # tech = SelectMultipleField(
    #     label="擅长领域",
    #     coerce=int,
    #     choices=[(1, 'python'), (2, 'linux'), (3, 'java'), (4, 'php'), (5, 'ruby'), (6, 'c++')]
    # )

    def validate_name(self, field):
        # field.data是用户输入的数据。
        if field.data == 'admin':
            # ValidationError从wtforms导入,用来向用户显示错误信息,
            # 验证函数的名称由validate_fieldname组成。
            raise ValidationError(u'超级管理员已被注册,换一个吧。')

    submit = SubmitField(label="注册")

