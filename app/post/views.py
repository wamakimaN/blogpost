from flask import Blueprint, flash,redirect,url_for,render_template,abort,request
from .form import PostForm,CommentForm
from flask_login import login_required, current_user
from ..models import Post,Comment
from flask_wtf import FlaskForm
from .. import db
from . import post

@post.route('/post/new', methods =['GET', 'POST'])
@login_required
def newpost():
    form = PostForm()
  
    if form.validate_on_submit():
        mypost = Post(title=form.title.data, content = form.content.data, summary = form.summary.data, author = current_user)
        db.session.add(mypost)
        db.session.commit()
        form_title = form.title.data
        print("title",form_title)
        flash('Your post has been created!', 'success')
        return redirect(url_for('main.index'))

    return render_template('post/newpost.html',post_form = form)

@post.route("/post/<int:post_id>", methods =['GET', 'POST'])
@login_required
def post(post_id):
 
    form = CommentForm()
    post = Post.query.get_or_404(post_id)
    comments = Comment.query.filter_by(post_id = post.id)
    if form.validate_on_submit():
        comment = Comment(post_id = post_id, description =form.description.data, author = current_user)
        db.session.add(comment)
        db.session.commit()
        flash('Your comment was added!', 'success')
        return redirect(url_for('post.post', post_id = post_id))
    
    
    return render_template('post/post.html', title=post.title, post=post,comment_form = form ,comments = comments)


