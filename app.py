#!/usr/bin/env python
# coding: utf-8

"""
CHURCH MANAGEMENT SYSTEM
Flood of Life Embazzy International Church
Flask-based web application
"""

# ===== IMPORTS =====
from flask import Flask, render_template, request, jsonify, redirect, url_for, session
import pandas as pd
import os
import json
import uuid
from datetime import datetime, timedelta

# ===== FLASK APP INITIALIZATION =====
app = Flask(__name__)
app.secret_key = "super-secret-key"  # Use environment variable in production

# ===== DATA FOLDER SETUP =====
DATA_FOLDER = 'church_data'
if not os.path.exists(DATA_FOLDER):
    os.makedirs(DATA_FOLDER)

# ===== PARTNERSHIP MANAGER =====
class PartnershipManager:
    """Manages church partners/members"""

    def __init__(self, data_file='partners.json'):
        self.data_file = os.path.join(DATA_FOLDER, data_file)
        self.partners = self.load_data()

    def load_data(self):
        """Load partners from file"""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as f:
                    return json.load(f)
            except json.JSONDecodeError:
                return []
        return []

    def save_data(self):
        """Save partners to file"""
        with open(self.data_file, 'w') as f:
            json.dump(self.partners, f, indent=2)

    def add_partner(self, name, email, phone, partnership_date):
        """Add a new partner"""
        partner = {
            'id': str(uuid.uuid4()),
            'name': name,
            'email': email,
            'phone': phone,
            'partnership_date': partnership_date,
            'created_at': datetime.now().isoformat()
        }
        self.partners.append(partner)
        self.save_data()
        return partner

    def get_all_partners(self):
        return self.partners

    def get_partner(self, partner_id):
        return next((p for p in self.partners if p['id'] == partner_id), None)

    def update_partner(self, partner_id, updates):
        partner = self.get_partner(partner_id)
        if partner:
            partner.update(updates)
            self.save_data()
        return partner

    def delete_partner(self, partner_id):
        self.partners = [p for p in self.partners if p['id'] != partner_id]
        self.save_data()

# Initialize manager
partner_manager = PartnershipManager()

# ===== ROUTES =====
@app.route('/')
def dashboard():
    return render_template('dashboard.html')

@app.route('/members')
def members():
    partners = partner_manager.get_all_partners()
    return render_template('members.html', partners=partners)

@app.route('/partnerships')
def partnerships():
    partners = partner_manager.get_all_partners()
    return render_template('partnerships.html', partners=partners)

# ===== API ROUTES =====
@app.route('/api/partners', methods=['GET'])
def api_get_partners():
    return jsonify(partner_manager.get_all_partners())

@app.route('/api/partners', methods=['POST'])
def api_add_partner():
    data = request.json
    partner = partner_manager.add_partner(
        name=data.get('name'),
        email=data.get('email'),
        phone=data.get('phone'),
        partnership_date=data.get('partnership_date')
    )
    return jsonify(partner)

@app.route('/api/partners/<partner_id>', methods=['PUT'])
def api_update_partner(partner_id):
    data = request.json
    partner = partner_manager.update_partner(partner_id, data)
    if partner:
        return jsonify(partner)
    return jsonify({"error": "Partner not found"}), 404

@app.route('/api/partners/<partner_id>', methods=['DELETE'])
def api_delete_partner(partner_id):
    partner_manager.delete_partner(partner_id)
    return jsonify({"message": "Partner deleted successfully"})

# ===== MAIN ENTRY =====
if __name__ == '__main__':
    app.run(debug=True)
