from flask import Flask, render_template, redirect
from markupsafe import escape
import jinja2

app = Flask(__name__)

navigation = [
    {
        "slide": 3,
        "href": "basic.html",
        "caption": "기본적인 HTML",
    },
    {
        "slide": 5,
        "href": "img.html",
        "caption": "이미지 태그",
    },
]


@app.route("/")
def index():
    nav = [
        dict(
            x.items(),
            **{
                "adjacent": {
                    "prev": navigation[i - 1] if i > 0 else "",
                    "next": navigation[i + 1] if i < len(navigation) - 1 else "",
                }
            }
        )
        for i, x in enumerate(navigation)
    ]
    print(nav)
    return render_template("index.html", navigation=nav)


@app.route("/<string:filename>")
def static_server(filename: str):
    if not filename.endswith(".html"):
        return render_template("404.html"), 404
    try:
        nav = [
            (
                (navigation[i - 1] if i > 0 else ""),
                x,
                (navigation[i + 1] if i < len(navigation) - 1 else ""),
            )
            for i, x in enumerate(navigation)
            if x["href"] == filename
        ][0]
        adjacent = {'prev': nav[0], 'cur': nav[1], 'next': nav[2]}
        return render_template(escape(filename), adjacent=adjacent)
    except jinja2.exceptions.TemplateNotFound:
        return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(debug=True)
