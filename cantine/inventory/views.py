from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from django.http import HttpResponse
from django.views.generic import ListView
from inventory.models import Product,Order,Cart

class Home(ListView):
    model = Product
    template_name = 'home.html'

@login_required
def add_to_cart(request, pk):
    item = get_object_or_404(Product, pk=pk)
    order_item, created = Cart.objects.get_or_create(
        item=item,
        user=request.user
    )
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.orderitems.filter(item__pk=item.pk).exists():
            order_item.quantity += 1
            order_item.save()
            #messages.success(request, "This item quantity was updated.")
            
            return redirect("cart")
        else:
            order.orderitems.add(order_item)
            #messages.info(request, "This item was added to your cart.")
            return redirect("home")
    else:
        order = Order.objects.create(
            user=request.user)
        order.orderitems.add(order_item)
        messages.info(request, "This item was added to your cart.")
        return redirect("home")


# Remove item from cart

def remove_from_cart(request, pk):
    item = get_object_or_404(Product, pk=pk)
    cart_qs = Cart.objects.filter(user=request.user, item=item)
    if cart_qs.exists():
        cart = cart_qs[0]
        # Checking the cart quantity
        if cart.quantity > 1:
            cart.quantity -= 1
            cart.save()
        else:
            cart_qs.delete()
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.orderitems.filter(item__pk=item.pk).exists():
            order_item = Cart.objects.filter(
                item=item,
                user=request.user,
            )[0]
            order.orderitems.remove(order_item)
            messages.info(request, "This item was removed from your cart.")
            return redirect("home")
        else:
            messages.info(request, "This item was not in your cart")
            return redirect("home")
    else:
        messages.info(request, "You do not have an active order")
        return redirect("home")



# Cart View

def CartView(request):

    user = request.user

    carts = Cart.objects.filter(user=user)
    orders = Order.objects.filter(user=user, ordered=False)

    if carts.exists():
        if orders.exists():
            order = orders[0]
            return render(request, 'cart.html', {"carts": carts, 'order': order})
        else:
            messages.warning(request, "You do not have an active order")
            return redirect("home")
            

    else:
        messages.warning(request, "You do not have an active order")
        return redirect("home")
        
        



##decrease item count from count
def decreaseCart(request, pk):
    item = get_object_or_404(Product, pk=pk)
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.orderitems.filter(item__pk=item.pk).exists():
            order_item = Cart.objects.filter(
                item=item,
                user=request.user
            )[0]
            if order_item.quantity > 1:
                order_item.quantity -= 1
                order_item.save()
            else:
                order.orderitems.remove(order_item)
                order_item.delete()
            messages.info(request, f"{item.name} quantity has updated.")
            return redirect("cart")
        else:
            messages.info(request, f"{item.name} quantity has updated.")
            return redirect("cart")
    else:
        messages.info(request, "You do not have an active order")
        return redirect("cart")


def checkout(request):
    order_m_t = Order.objects.get(user=request.user, ordered=False)
    order_m_t.ordered = True
    order_m_t.save()
    
    user = request.user

    carts = Cart.objects.filter(user=user)
    orders = Order.objects.filter(user=user, ordered=True)

    if carts.exists():
        if orders.exists():
            order = orders[0]
            return render(request, 'order_placed.html', {"carts": carts, 'order': order})
        else:
            messages.warning(request, "You do not have an active order")
            return redirect("home")
            

    else:
        messages.warning(request, "You do not have an active order")
        return redirect("home")

    



