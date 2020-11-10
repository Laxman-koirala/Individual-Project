from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView, DetailView
from .models import Post
from itertools import chain
from User.models import Profile
import datetime
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

@method_decorator(login_required, name='dispatch')
class ProfileListView(ListView):
    model = Profile
    template_name = 'Blog/personYouMayKnow.html'
    context_object_name = 'profiles'

    def get_queryset(self):
        return Profile.objects.all().exclude(user=self.request.user)

@method_decorator(login_required, name='dispatch')
class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'Blog/profile.html'
    context_object_name = 'profiles'

    def get_object(self, **kwargs):
        pkg = self.kwargs.get('pk')
        view_profile = Profile.objects.get(pk=pkg)
        return view_profile


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        view_profile = self.get_object()

        my_profile = Profile.objects.get(user=self.request.user)
        if view_profile.user in my_profile.following.all():
            follow = True
        else:
            follow = False
        context['follow'] = follow

        return context


@login_required
def follow_and_unfollow(request):
    if request.method == 'POST':
        my_profile = Profile.objects.get(user=request.user)
        pk = request.POST.get('profile_pk')
        obj = Profile.objects.get(pk=pk)

        if obj.user in my_profile.following.all():
            my_profile.following.remove(obj.user)

        else:
            my_profile.following.add(obj.user)
    return redirect(request.META.get('HTTP_REFERER'))

@login_required
def Posts_following(request):
    profile = Profile.objects.get(user=request.user)
    user = [user for user in profile.following.all()]
    posts = []
    qs = None
    for u in user:
        p = Profile.objects.get(user=u)
        p_posts = p.post_set.all()
        posts.append(p_posts)
    my_posts =profile.profiles_posts()
    posts.append(my_posts)

    if len(posts)>0:
        qs = sorted(chain(*posts),reverse=True, key = lambda obj: obj.time_upload)

    return render(request,'Blog/newsfeed.html',{'posts':qs})

@login_required
def Trending(request):
    time =datetime.date.today()-datetime.timedelta(days=20)
    trends = Post.objects.filter(time_upload__gte = time).order_by('-view')
    contex={
     'trend':trends[:20],
    }
    return render(request,'Blog/trending.html',contex)
@login_required
def Popular (request):
    time =datetime.date.today()-datetime.timedelta(days=365)
    popu = Post.objects.filter(time_upload__gte = time).order_by('-view')
    contex = {
    'trend': popu,
    }
    return render(request,'Blog/popular.html',contex)


@method_decorator(login_required, name='dispatch')
class CreatePost(CreateView):
    model = Post
    fields = ['title', 'overview','thumbnail','categories']
    template_name = 'Blog/post.html'
    success_url = '/newsfeed/'
    context_object_name = 'form'

    def form_valid(self, form):
        user = Profile.objects.get(user=self.request.user)
        form.instance.Author = user
        return super(CreatePost, self).form_valid(form)


@method_decorator(login_required, name='dispatch')
class profileEdit(UpdateView):
    model =  Profile
    fields = ['bio', 'photo']
    template_name = 'Blog/profileEdit.html'
    success_url = '/newsfeed/'
    context_object_name = 'form'
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

@login_required
def profileuser():
    me = Profile.objects.get(user=request.user)
    lookup_field = 'pk'
    contex={
     'u':me.pk,
    }

    return render(request,'Blog/base.html',contex)

@login_required
def search(request):
    searchfor = request.GET.get('find')
    posts = Post.objects.filter(
        Q(title__icontains = searchfor) |
        Q(overview__icontains = searchfor) |
        Q(Author__user__username__icontains = searchfor)

        ).distinct()
    contex = {
    'posts':posts,
    'title':f'Searching result for {searchfor}'
    }
    return render(request,'Blog/search.html',contex)
