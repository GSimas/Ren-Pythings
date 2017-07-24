image bg meadow = "meadow.jpg"
image bg uni = "uni.jpg"

image sylvie smile = "sylvie_smile.png"
image sylvie surprised = "sylvie_surprised.png"

define s = Character('Sylvie', color="#c8ffc8")
define m = Character('Me', color="#c8c8ff")

label splashscreen:
    show bg meadow
    $ renpy.pause(2.0)
    return
    
label start:
    scene bg uni
    show sylvie smile
    
    s "Oh, hi, do we walk home together?"
    m "Yes..."
    "I said and my voice was already shaking."
    
    scene bg meadow
    with fade
    
    "We reached the meadows just outside our hometown."
    "Autumn was so beautiful here."
    "When we were children, we often played here."
    m "Hey... umm..."
    
    show sylvie smile
    with dissolve
    
    "She turned to me and smiled"
    "I'll ask her..."
    
    m "Um... will you..."
    m "Will you be my artist for a visual novel?"
    
    show sylvie surprised at right
    
    "Silence."
    "She is shocked, and then..."
    
    show sylvie smile
    
    s "Sure, but what is a \"visual novel?\""