from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/json', methods=['GET'])
def get_json():
    data = {
        'message': 'Hello, World!',
        'status': 'success'
    }
    return jsonify(data)

@app.route('/', methods=['GET'])
def provide():
    return '<h1>Hello, World!</h1>'

@app.route('/html', methods=['GET'])
def get_html():
    return '<h1>menutest</h1>'

@app.route('/menudata', methods=['GET'])    
def give_menu():
    data = {
  "tax_rates": [
    {
      "external_id": "79b5fc81",
      "name": "Default Tax Rate",
      "rate": 0.05,
      "included_in_item_price": True,
      "valid": True
    }
  ],
  "schedules": [
    {
      "external_id": "826991a0",
      "rules": [
        {
          "days": [
            "SUNDAY"
          ],
          "start": "07:00:00.000",
          "end": "19:00:00.000"
        },
        {
          "days": [
            "MONDAY"
          ],
          "start": "07:00:00.000",
          "end": "19:00:00.000"
        }
      ],
      "sections": [
        {
          "external_id": "79ffafb1",
          "name": "APPETIZERS",
          "description": "APPETIZERS",
          "items": [
            {
              "external_id": "79fb9101",
              "metadata": "metadata",
              "name": "Antipasto Misto",
              "description": "Brick oven-roasted peppers, zucchini, artichokes, olives, prosciutto, fresh asparagus, broccoli, fresh mozzarella and grape tomatoes served with baby field greens and balsamic vinaigrette. ",
              "calorie_content": "100",
              "minimum_serving_size": 0,
              "maximum_serving_size": 0,
              "minimum_order_quantity": 1,
              "media": "http://some.image.com/123",
              "tax_rate": "79b5fc81",
              "price": 399.0,
              "excludes_coupons": False,
              "size_prompt": {
                "external_id": "80747863",
                "name": "Choose a size",
                "sizes": [
                  {
                    "external_id": "21b83e1f",
                    "name": "Small",
                    "price": 2.99,
                    "calorie_content": "150"
                  },
                  {
                    "external_id": "fbd68d5f",
                    "name": "Large",
                    "price": 4.99,
                    "calorie_content": "250"
                  }
                ]
              },
              "deal": True,
              "tags": [
                {
                  "group": "LEGACY",
                  "name": "SODIUM_WARNING"
                }
              ],
              "modifier_categories": [
                {
                  "external_id": "79f416f0",
                  "name": "Antipasto Misto Remove Ingredients",
                  "min": 0,
                  "max": 8,
                  "included": 0,
                  "batch_quantity": 1,
                  "maximum_modifier_quantity": 1,
                  "price_adjustment": {
                    "type": "ADD",
                    "value": 0.5
                  },
                  "modifiers": [
                    {
                      "external_id": "79e23ca1",
                      "metadata": "metadata",
                      "name": "NO OLIVES",
                      "price": 0.0,
                      "calorie_content": "100",
                      "sized_prices": []
                    },
                    {
                      "external_id": "79e45f81",
                      "name": "NO DRESSING",
                      "description": "NO DRESS",
                      "price": 0.0,
                      "calorie_content": "100",
                      "sized_prices": []
                    }
                  ]
                }
              ]
            },
            {
              "external_id": "79fc5451",
              "name": "Mozzarella Fritta",
              "description": "Breaded mozzarella pan-fried in extra-virgin olive oil served over plum tomato sauce with fresh basil. \r\n",
              "calorie_content": "100",
              "minimum_serving_size": 0,
              "maximum_serving_size": 0,
              "minimum_order_quantity": 1,
              "tax_rate": "79b5fc81",
              "price": 799.0,
              "excludes_coupons": False,
              "coupons": [],
              "tags": [],
              "modifier_categories": []
            }
          ]
        },
        {
          "external_id": "7a1d22c0",
          "name": "SPECIALTIES",
          "items": [
            {
              "external_id": "7a16e131",
              "name": "Grilled Steak & Chicken Combo*",
              "description": "A combination of 6 oz. of sliced flat iron steak and a lemon-thyme chicken breast over tomatoes. Served with mashed potatoes and fresh asparagus. ",
              "calorie_content": "100",
              "minimum_serving_size": 0,
              "maximum_serving_size": 0,
              "minimum_order_quantity": 1,
              "tax_rate": "79b5fc81",
              "price": 1799.0,
              "excludes_coupons": False,
              "coupons": [],
              "tags": [],
              "modifier_categories": [
                {
                  "external_id": "7a142211",
                  "name": "Meat Temperature",
                  "min": 0,
                  "max": 5,
                  "included": 0,
                  "batch_quantity": 1,
                  "maximum_modifier_quantity": 1,
                  "modifiers": [
                    {
                      "external_id": "7a1337b1",
                      "name": "RARE",
                      "description": "**  RARE **",
                      "price": 0.0,
                      "calorie_content": "100",
                      "sized_prices": []
                    },
                    {
                      "external_id": "7a135ec1",
                      "name": "MEDIUM RARE",
                      "description": "**MED RARE**",
                      "price": 0.0,
                      "calorie_content": "100",
                      "sized_prices": []
                    },
                    {
                      "external_id": "7a13ace0",
                      "name": "MEDIUM",
                      "description": "** MEDIUM **",
                      "price": 0.0,
                      "calorie_content": "100",
                      "sized_prices": []
                    },
                    {
                      "external_id": "7a13d3f1",
                      "name": "MEDIUM WELL",
                      "description": "**MED WELL**",
                      "price": 0.0,
                      "calorie_content": "100",
                      "sized_prices": []
                    },
                    {
                      "external_id": "7a13fb01",
                      "name": "WELL DONE",
                      "description": "**WEL DONE**",
                      "price": 0.0,
                      "calorie_content": "100",
                      "sized_prices": []
                    }
                  ]
                }
              ]
            }
          ]
        }
      ]
    }
  ]}
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
