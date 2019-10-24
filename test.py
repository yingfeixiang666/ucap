# coding: utf-8
from sqlalchemy import Column, Date, DateTime, Integer, String
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class SysRole(db.Model):
    __tablename__ = 'sys_role'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255, 'utf8_general_ci'))
    description = db.Column(db.String(255, 'utf8_general_ci'))
    status = db.Column(db.Integer)
    oper = db.Column(db.Integer)
    modify_time = db.Column(db.DateTime)
    create_time = db.Column(db.DateTime)


class SysUser(db.Model):
    __tablename__ = 'sys_user'

    id = db.Column(db.Integer, primary_key=True)
    account = db.Column(db.String(255, 'utf8_general_ci'))
    name = db.Column(db.String(255, 'utf8_general_ci'))
    password = db.Column(db.String(255, 'utf8_general_ci'))
    deptId = db.Column(db.Integer)
    phone = db.Column(db.String(255, 'utf8_general_ci'))
    email = db.Column(db.String(255, 'utf8_general_ci'))
    sex = db.Column(db.Integer)
    birth = db.Column(db.Date)
    picId = db.Column(db.Integer)
    liveAddress = db.Column(db.String(255, 'utf8_general_ci'))
    hobby = db.Column(db.String(255, 'utf8_general_ci'))
    province = db.Column(db.String(255, 'utf8_general_ci'))
    city = db.Column(db.String(255, 'utf8_general_ci'))
    county = db.Column(db.String(255, 'utf8_general_ci'))
    remarks = db.Column(db.String(255, 'utf8_general_ci'))
    updateBy = db.Column(db.Integer)
    createBy = db.Column(db.Integer)
    create_time = db.Column(db.DateTime)
    modify_time = db.Column(db.DateTime)
    del_flag = db.Column(db.Integer)
