# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 19:56:16 2020

@author: Asus
"""

from flask import Flask , request, jsonify
import json
import sqlite3

app = Flask(__name__)

def db_connection():
    conn = None
    try:
        conn = sqlite3.connect("Sales.db")
    except sqlite3.error as e:
        print(e)
    return conn



@app.route("/SalesCube", methods=["GET"])
def manyItems():
    conn = db_connection()
    cursor = conn.cursor()

    if request.method == "GET":
        cursor = conn.execute("SELECT * FROM SalesCube")
        SalesCube = [
            dict(Products=row[0], OrderDate=row[1], ProductsDescription=row[2], ProductCategory=row[3], ManufacturedCountry=row[4] ,
             ProductCost = row[5],CustomerID = row[6],SalePricePerPiece=row[7],QuantityPurchased=row[8],Currency=row[9],
             CustomerCity = row[10], Latitude=row[11]  , Longitude=row[12] , Country=row[13] , CountryCode=row[14] ,
             EID=row[15], Employee_FirstName=row[16], Employee_LastName=row[17] , Employee_Gender=row[18], SaleXpLevel=row[19],
             Ratings=row[21],OrderNr=row[22]
                 )
            for row in cursor.fetchall()
        ]
        if manyItems is not None:
            return jsonify(SalesCube)

   
    
    
@app.route("/SalesCube/<string:OrderNr>", methods=["GET", "PUT", "DELETE"])
def single_item(OrderNr):
    conn = db_connection()
    cursor = conn.cursor()
    Cubes = None
    if request.method == "GET":
        cursor.execute("SELECT * FROM SalesCube WHERE OrderNr=?", (OrderNr,))
        rows = cursor.fetchall()
        for r in rows:
            Cubes = r
        if Cubes is not None:
            return jsonify(Cubes), 200
        else:
            return "Something wrong", 404
        
if __name__ == "__main__":
     app.run(host='127.0.0.1', port=8443)
