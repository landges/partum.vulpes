from app import app, db
from flask import render_template, redirect, flash, request
from .forms import OrderForm
from .models import Product, ProductInOrder, Order


def create_producr(name,price,time,image):
    u = Product(name=name,
                price=price,
                time=time,
                image=image)
    db.session.add(u)
    db.session.commit()

@app.route('/')
@app.route('/index')
def index():
    form = OrderForm()
    products = db.session.query(Product).all()
    orders = db.session.query(Order).all()
    # print(orders[0].email)
    return render_template('index.html', title='Home', products=products, form=form)


@app.route('/order', methods=['POST'])
def order():
    form = OrderForm()
    if form.validate_on_submit():
        print(form.name.data)
        print('here')
        order = Order(username=form.name.data,
                      email=form.email.data,
                      phone=form.phone.data,
                      content=form.content.data)
        db.session.add(order)
        db.session.commit()
        # flash('Login requested for user {}, remember_me={}'.format(
        #     form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('index.html', title='Sign In', form=form)