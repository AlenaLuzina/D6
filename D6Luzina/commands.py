from newapp.models import *

u1 = User.objects.create_user(username = 'Semyon')
u2 = User.objects.create_user(username = 'Sam')

a1 = Author.objects.create(authorUser=u1)
a2 = Author.objects.create(authorUser=u2)

IT = Category.objects.create(name='IT')
Category.objects.create(name='Politics')
Category.objects.create(name='Business')
Category.objects.create(name='Science')
Category.objects.create(name='Health')
Category.objects.create(name='Arts')
Category.objects.create(name='Books')
Category.objects.create(name='Style')
Category.objects.create(name='Food')
Category.objects.create(name='Travel')

Post.objects.create(author=a1, categoryType='NW', title = 'sometitle', text = 'somebigtext')
Post.objects.create(author=a1, categoryType='AR', title = 'Article about Business', text = 'somebigtext about Business')
Post.objects.create(author=a2, categoryType='AR', title = 'How i`m learning Python', text = 'I do it with help of SkillFactory')


Post.objects.get(id=1).postCategory.add(Category.objects.get(id=1))
Post.objects.get(id=1).postCategory.add(Category.objects.get(id=9))
Post.objects.get(id=1).postCategory.add(Category.objects.get(id=10))
Post.objects.get(id=2).postCategory.add(Category.objects.get(id=3))
Post.objects.get(id=2).postCategory.add(Category.objects.get(id=4))
Post.objects.get(id=3).postCategory.add(Category.objects.get(id=1))
Post.objects.get(id=3).postCategory.add(Category.objects.get(id=4))

Comment.objects.create(commentPost=Post.objects.get(id=1),commentUser=Author.objects.get(id=1).authorUser, text='Somecommenttext')
Comment.objects.create(commentPost=Post.objects.get(id=2),commentUser=Author.objects.get(id=2).authorUser, text='Everyone should understand economics')
Comment.objects.create(commentPost=Post.objects.get(id=2),commentUser=Author.objects.get(id=1).authorUser, text='Economics is about each country ')
Comment.objects.create(commentPost=Post.objects.get(id=3),commentUser=Author.objects.get(id=1).authorUser, text='I`m learning Python too!')
Comment.objects.get(id=1).Like()
Comment.objects.get(id=1).Like()
Comment.objects.get(id=1).Like()
Comment.objects.get(id=2).Like()
Comment.objects.get(id=2).Like()
Comment.objects.get(id=2).Like()
Comment.objects.get(id=2).Like()
Comment.objects.get(id=3).Like()
Comment.objects.get(id=3).Like()
Comment.objects.get(id=1).Dislike()
Comment.objects.get(id=1).Dislike()
Comment.objects.get(id=1).Dislike()
Comment.objects.get(id=2).Dislike()

Post.objects.get(id=1).Like()
Post.objects.get(id=1).Like()
Post.objects.get(id=2).Like()
Post.objects.get(id=3).Disike()
Post.objects.get(id=5).Like()

Author.objects.get(id=1).update_rating()
Author.objects.get(id=2).update_rating()

Author.objects.get(id=1).ratingAuthor
Author.objects.get(id=2).ratingAuthor

best=Author.objects.all().order_by('-ratingAuthor').values('authorUser', 'ratingAuthor')[0]
print(best)

bestpost=Post.objects.all().order_by('-rating').values('dateCreation', 'author','rating','title', 'text')[0]
print(bestpost)

p1 = Post.objects.get(id=1)
allcomments=Comment.objects.filter(commentPost = p1).values('dateCreation', 'commentUser','rating','text')
print(allcomments)