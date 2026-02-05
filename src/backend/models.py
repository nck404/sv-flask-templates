from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    last_login_ip = db.Column(db.String(45))
    avatar_url = db.Column(db.String(255), nullable=True)
    username_last_updated = db.Column(db.DateTime, nullable=True)
    
    bio = db.Column(db.Text, nullable=True)
    job_title = db.Column(db.String(100), nullable=True)
    links = db.Column(db.JSON, nullable=True)


    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "last_login_ip": self.last_login_ip,
            "avatar_url": self.avatar_url,
            "username_last_updated": self.username_last_updated.isoformat() if self.username_last_updated else None,
            "bio": self.bio,
            "job_title": self.job_title,
            "links": self.links
        }


class Lesson(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    situation = db.Column(db.String(100), nullable=False)
    gesture_target = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=True)
    karaoke_content = db.Column(db.JSON, nullable=True)
    lesson_type = db.Column(db.String(50), default='sign_language')
    video_id = db.Column(db.String(50), nullable=True)



    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "situation": self.situation,
            "gesture_target": self.gesture_target,
            "description": self.description,
            "karaoke_content": self.karaoke_content,
            "lesson_type": self.lesson_type,
            "video_id": self.video_id
        }



class UserProgress(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    lesson_id = db.Column(db.Integer, db.ForeignKey('lesson.id'), nullable=False)
    completed_at = db.Column(db.DateTime, server_default=db.func.now())

    user = db.relationship('User', backref=db.backref('progress', lazy=True))
    lesson = db.relationship('Lesson', backref=db.backref('completions', lazy=True))

class BlogTopic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    description = db.Column(db.String(200))

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description
        }

class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    image_data = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    topic_id = db.Column(db.Integer, db.ForeignKey('blog_topic.id'), nullable=True)

    author = db.relationship('User', backref=db.backref('posts', lazy=True))
    topic = db.relationship('BlogTopic', backref=db.backref('posts', lazy=True))

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "content": self.content,
            "image_data": self.image_data,
            "created_at": self.created_at.isoformat(),
            "author": self.author.username if self.author else "Người dùng cũ",
            "author_id": self.author_id,
            "author_avatar": self.author.avatar_url if self.author else None,
            "topic": self.topic.name if self.topic else None,
            "comment_count": len(self.comments)


        }

class BlogComment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('blog_post.id'), nullable=False)
    parent_id = db.Column(db.Integer, db.ForeignKey('blog_comment.id'), nullable=True)

    author = db.relationship('User', backref=db.backref('blog_comments', lazy=True))
    post = db.relationship('BlogPost', backref=db.backref('comments', lazy=True))
    replies = db.relationship('BlogComment', backref=db.backref('parent', remote_side=[id]), lazy=True)

    def to_dict(self):
        return {
            "id": self.id,
            "content": self.content,
            "created_at": self.created_at.isoformat(),
            "author": self.author.username,
            "author_avatar": self.author.avatar_url,
            "parent_id": self.parent_id
        }

