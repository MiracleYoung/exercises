```flow
s=>start: Start
e=>end: End
cond=>condition: Is Allowed?
apply=>operation: Apply Register
audit=>operation: Admin Audit
form=>operation: Staff Get Authority and Fill out Form
s->apply->audit->cond
cond(yes)->form->e
cond(no)->e
```
