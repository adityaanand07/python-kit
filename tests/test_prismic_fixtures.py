#!/usr/bin/env python
# -*- coding: utf-8 -*-

api_sample_data = """
{
    "refs": [{
        "ref": "UgjWQN_mqa8HvPJY",
        "label": "Master",
        "isMasterRef": true
    }, {
        "ref": "UgjWRd_mqbYHvPJa",
        "label": "San Francisco Grand opening"
    }],
    "bookmarks": {
        "about": "Ue0EDd_mqb8Dhk3j",
        "jobs": "Ue0EHN_mqbwDhk3l",
        "stores": "Ue0EVt_mqd8Dhk3n"
    },
    "types": {
        "blog-post": "Blog post",
        "store": "Store",
        "article": "Site-level article",
        "selection": "Products selection",
        "job-offer": "Job offer",
        "product": "Product"
    },
    "tags": ["Cupcake", "Pie", "Featured", "Macaron"],
    "forms": {
        "everything": {
            "method": "GET",
            "enctype": "application/x-www-form-urlencoded",
            "action": "http://lesbonneschoses.wroom.io/api/documents/search",
            "fields": {
                "ref": {
                    "type": "String"
                },
                "q": {
                    "type": "String"
                }
            }
        }
    },
    "oauth_initiate": "http://lesbonneschoses.wroom.io/auth",
    "oauth_token": "http://lesbonneschoses.wroom.io/auth/token"
}"""
search_sample_data = """[
    {
        "id": "UdUkXt_mqZBObPeS",
        "type": "product",
        "href": "http://lesbonneschoses.wroom.io/api/documents/search?ref=UgjWQN_mqa8HvPJY&q=%5B%5B%3Ad+%3D+at%28document.id%2C+%22UdUkXt_mqZBObPeS%22%29+%5D%5D",
        "tags": [
            "Macaron"
        ],
        "slugs": [
            "vanilla-macaron"
        ],
        "data": {
            "product": {
                "image": {
                    "type": "Image",
                    "value": {
                        "main": {
                            "url": "https://wroomio.s3.amazonaws.com/lesbonneschoses/0417110ebf2dc34a3e8b7b28ee4e06ac82473b70.png",
                            "dimensions": {
                                "width": 500,
                                "height": 500
                            }
                        },
                        "views": {
                            "icon": {
                                "url": "https://wroomio.s3.amazonaws.com/lesbonneschoses/babdc3421037f9af77720d8f5dcf1b84c912c6ba.png",
                                "dimensions": {
                                    "width": 250,
                                    "height": 250
                                }
                            }
                        }
                    }
                },
                "short_lede": {
                    "type": "StructuredText",
                    "value": [
                        {
                            "type": "heading2",
                            "text": "Crispiness and softness, rolled into one",
                            "spans": []
                        }
                    ]
                },
                "description": {
                    "type": "StructuredText",
                    "value": [
                        {
                            "type": "paragraph",
                            "text": "Experience the ultimate vanilla experience. Our vanilla Macarons are made with our very own (in-house) pure extract of Madagascar vanilla, and subtly dusted with our own vanilla sugar (which we make from real vanilla beans).",
                            "spans": [
                                {
                                    "start": 103,
                                    "end": 137,
                                    "type": "strong"
                                },
                                {
                                    "start": 162,
                                    "end": 183,
                                    "type": "strong"
                                }
                            ]
                        }
                    ]
                },
                "testimonial_author": [
                    {
                        "type": "StructuredText",
                        "value": [
                            {
                                "type": "heading3",
                                "text": "Chef Guillaume Bort",
                                "spans": []
                            }
                        ]
                    }
                ],
                "testimonial_quote": [
                    {
                        "type": "StructuredText",
                        "value": [
                            {
                                "type": "paragraph",
                                "text": "The taste of pure vanilla is very hard to tame, and therefore, most cooks resort to substitutes. It takes a high-skill chef to know how to get the best of tastes, and Les Bonnes Choses's vanilla macaron does just that. The result is more than a success, it simply is a gastronomic piece of art.",
                                "spans": [
                                    {
                                        "start": 97,
                                        "end": 167,
                                        "type": "strong"
                                    },
                                    {
                                        "start": 167,
                                        "end": 184,
                                        "type": "strong"
                                    },
                                    {
                                        "start": 167,
                                        "end": 184,
                                        "type": "em"
                                    },
                                    {
                                        "start": 184,
                                        "end": 217,
                                        "type": "strong"
                                    }
                                ]
                            }
                        ]
                    }
                ],
                "related": [
                    {
                        "type": "Link.document",
                        "value": {
                            "document": {
                                "id": "UdUjvt_mqVNObPeO",
                                "type": "product",
                                "tags": [
                                    "Macaron"
                                ],
                                "slug": "dark-chocolate-macaron"
                            },
                            "isBroken": false
                        }
                    },
                    {
                        "type": "Link.document",
                        "value": {
                            "document": {
                                "id": "UdUjsN_mqT1ObPeM",
                                "type": "product",
                                "tags": [
                                    "Macaron"
                                ],
                                "slug": "salted-caramel-macaron"
                            },
                            "isBroken": false
                        }
                    }
                ],
                "price": {
                    "type": "Number",
                    "value": 3.55
                },
                "color": {
                    "type": "Color",
                    "value": "#ffeacd"
                },
                "flavour": [
                    {
                        "type": "Select",
                        "value": "Vanilla"
                    }
                ],
                "name": {
                    "type": "StructuredText",
                    "value": [
                        {
                            "type": "heading1",
                            "text": "Vanilla Macaron",
                            "spans": []
                        }
                    ]
                },
                "allergens": {
                    "type": "Text",
                    "value": "Contains almonds, eggs, milk"
                }
            }
        }
    },
    {
        "id": "UdUjsN_mqT1ObPeM",
        "type": "product",
        "href": "http://lesbonneschoses.wroom.io/api/documents/search?ref=UgjWQN_mqa8HvPJY&q=%5B%5B%3Ad+%3D+at%28document.id%2C+%22UdUjsN_mqT1ObPeM%22%29+%5D%5D",
        "tags": [
            "Macaron"
        ],
        "slugs": [
            "salted-caramel-macaron"
        ],
        "data": {
            "product": {
                "image": {
                    "type": "Image",
                    "value": {
                        "main": {
                            "url": "https://wroomio.s3.amazonaws.com/lesbonneschoses/06074de2d9590adddcdb50547108d811af0d9913.png",
                            "dimensions": {
                                "width": 500,
                                "height": 500
                            }
                        },
                        "views": {
                            "icon": {
                                "url": "https://wroomio.s3.amazonaws.com/lesbonneschoses/7accefd1e7204bbca06e8f13b8ef25fdb673ec67.png",
                                "dimensions": {
                                    "width": 250,
                                    "height": 250
                                }
                            }
                        }
                    }
                },
                "short_lede": {
                    "type": "StructuredText",
                    "value": [
                        {
                            "type": "heading2",
                            "text": "Salty-sweety, evermore melty",
                            "spans": []
                        }
                    ]
                },
                "description": {
                    "type": "StructuredText",
                    "value": [
                        {
                            "type": "paragraph",
                            "text": "It's no wonder why our \\"Salted Caramel French Macaron\\" has become our best-selling macaron: on top of the authentic Parisian preparation that has been making our macarons so popular and enjoyed by gourmets, you can also feel the waves of Britanny's ocean as you bite into it. Two of the best French local gastronomies meet in your mouth, and suddenly, it's like French Revolution all over again, contained in a single macaron.",
                            "spans": []
                        }
                    ]
                },
                "testimonial_author": [
                    {
                        "type": "StructuredText",
                        "value": [
                            {
                                "type": "heading3",
                                "text": "Chef Drobi",
                                "spans": []
                            }
                        ]
                    },
                    {
                        "type": "StructuredText",
                        "value": [
                            {
                                "type": "heading3",
                                "text": "Chef Guergachi",
                                "spans": []
                            }
                        ]
                    }
                ],
                "testimonial_quote": [
                    {
                        "type": "StructuredText",
                        "value": [
                            {
                                "type": "paragraph",
                                "text": "You have never known macarons, unless you have tasted Les Bonnes Choses's signature macaron! Salted caramel is very addictive, and even more so when treated with such high standards and respect for the raw material. This is the single best pastry you may taste before long.",
                                "spans": [
                                    {
                                        "start": 54,
                                        "end": 71,
                                        "type": "em"
                                    },
                                    {
                                        "start": 216,
                                        "end": 272,
                                        "type": "strong"
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "type": "StructuredText",
                        "value": [
                            {
                                "type": "paragraph",
                                "text": "Try Les Bonnes Choses's salty caramel macaron, and I personally guarantee that you will be grateful to yourself! This is the only dessert I serve in my restaurant which isn't prepared in my own kitchens, and yet, it is always the one I advise first to my most hesitant clients for their dessert. Let's be honest: that way, I just know I'm getting a customer back within weeks...",
                                "spans": [
                                    {
                                        "start": 4,
                                        "end": 21,
                                        "type": "em"
                                    },
                                    {
                                        "start": 51,
                                        "end": 112,
                                        "type": "strong"
                                    }
                                ]
                            }
                        ]
                    }
                ],
                "related": [
                    {
                        "type": "Link.document",
                        "value": {
                            "document": {
                                "id": "UdUjvt_mqVNObPeO",
                                "type": "product",
                                "tags": [
                                    "Macaron"
                                ],
                                "slug": "dark-chocolate-macaron"
                            },
                            "isBroken": false
                        }
                    },
                    {
                        "type": "Link.document",
                        "value": {
                            "document": {
                                "id": "UdUkXt_mqZBObPeS",
                                "type": "product",
                                "tags": [
                                    "Macaron"
                                ],
                                "slug": "vanilla-macaron"
                            },
                            "isBroken": false
                        }
                    },
                    {
                        "type": "Link.document",
                        "value": {
                            "document": {
                                "id": "UdUoc9_mqRlQbPeU",
                                "type": "product",
                                "tags": [
                                    "Macaron"
                                ],
                                "slug": "pistachio-macaron"
                            },
                            "isBroken": false
                        }
                    }
                ],
                "price": {
                    "type": "Number",
                    "value": 3.5
                },
                "color": {
                    "type": "Color",
                    "value": "#db6e09"
                },
                "flavour": [
                    {
                        "type": "Select",
                        "value": "Salted caramel"
                    },
                    {
                        "type": "Select",
                        "value": ""
                    }
                ],
                "name": {
                    "type": "StructuredText",
                    "value": [
                        {
                            "type": "heading1",
                            "text": "Salted Caramel Macaron",
                            "spans": []
                        }
                    ]
                },
                "allergens": {
                    "type": "Text",
                    "value": "Contains almonds, eggs and milk"
                }
            }
        }
    },
    {
        "id": "UebQ4N_mqYEJYF7N",
        "type": "product",
        "href": "http://lesbonneschoses.wroom.io/api/documents/search?ref=UgjWQN_mqa8HvPJY&q=%5B%5B%3Ad+%3D+at%28document.id%2C+%22UebQ4N_mqYEJYF7N%22%29+%5D%5D",
        "tags": [
            "Pie"
        ],
        "slugs": [
            "cherry-lime-pie"
        ],
        "data": {
            "product": {
                "image": {
                    "type": "Image",
                    "value": {
                        "main": {
                            "url": "https://wroomio.s3.amazonaws.com/lesbonneschoses/d88b287f7971c0d5f6d17c90176ac186fcd5ba22.png",
                            "dimensions": {
                                "width": 500,
                                "height": 500
                            }
                        },
                        "views": {
                            "icon": {
                                "url": "https://wroomio.s3.amazonaws.com/lesbonneschoses/4a4acae4e5f3dd466ba2d8c9d2083a411439431d.png",
                                "dimensions": {
                                    "width": 250,
                                    "height": 250
                                }
                            }
                        }
                    }
                },
                "short_lede": {
                    "type": "StructuredText",
                    "value": [
                        {
                            "type": "heading2",
                            "text": "Sweet and sour, but mostly sweet",
                            "spans": []
                        }
                    ]
                },
                "description": {
                    "type": "StructuredText",
                    "value": [
                        {
                            "type": "paragraph",
                            "text": "Cherry flavour in pastries is always a bit aggressive, and usually doesn't care much to let other tastes express themselves. But today, cherry is meeting an opponent who's very able to challenge him: pure Italian-imported lime! As they fight for their right to let you experience their magic the result is an explosion of opposing tastes in your mouth! Chocolate dust will serve as the palate-awakening judge of this heated encounter, while the cherry will attempt to display its domination by sitting on the boxing ring.",
                            "spans": []
                        }
                    ]
                },
                "testimonial_author": [
                    {
                        "type": "StructuredText",
                        "value": [
                            {
                                "type": "heading3",
                                "text": "Chef Crème",
                                "spans": []
                            }
                        ]
                    },
                    {
                        "type": "StructuredText",
                        "value": [
                            {
                                "type": "heading3",
                                "text": "Chef Drobi",
                                "spans": []
                            }
                        ]
                    }
                ],
                "testimonial_quote": [
                    {
                        "type": "StructuredText",
                        "value": [
                            {
                                "type": "paragraph",
                                "text": "If you're looking for one of Les Bonnes Choses's notoriously daring masterpieces... look no more! Whatever your experience with pastry, this will unsettle you, to a point where you'll wonder whether pastry can be taken further than this bold piece of art. To be urgently advised to anyone who believes that pastry can not be an experience by itself.",
                                "spans": [
                                    {
                                        "start": 29,
                                        "end": 46,
                                        "type": "em"
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "type": "StructuredText",
                        "value": [
                            {
                                "type": "paragraph",
                                "text": "I've had my share of fruit-combination attempts, and lime was always last on my list to combine with berries, because it just seemed wrong. It took a great pastry house like Les Bonnes Choses to suppress my taboo, and realize that what once seems wrong, can later seem insanely right!",
                                "spans": [
                                    {
                                        "start": 174,
                                        "end": 191,
                                        "type": "em"
                                    }
                                ]
                            }
                        ]
                    }
                ],
                "price": {
                    "type": "Number",
                    "value": 3
                },
                "color": {
                    "type": "Color",
                    "value": "#e9221d"
                },
                "flavour": [
                    {
                        "type": "Select",
                        "value": "Lemon/lime"
                    },
                    {
                        "type": "Select",
                        "value": "Berries"
                    }
                ],
                "name": {
                    "type": "StructuredText",
                    "value": [
                        {
                            "type": "heading1",
                            "text": "Cherry-Lime Pie",
                            "spans": []
                        }
                    ]
                },
                "allergens": {
                    "type": "Text",
                    "value": "Contains lime, milk and eggs."
                }
            }
        }
    }
]"""