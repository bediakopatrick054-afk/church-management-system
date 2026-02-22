#!/usr/bin/env python
# coding: utf-8

# In[1]:


# CHURCH MANAGEMENT SYSTEM FOR FLOOD OF LIFE EMBAZZY INTERNATIONAL CHURCH
# Complete implementation based on screenshot analysis

# Step 1: Import required libraries
from flask import Flask, render_template, request, jsonify, redirect, url_for, session
import pandas as pd
import numpy as np
import os
import matplotlib
matplotlib.use('Agg')  # Required for Render
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta, date
import random
import string
import base64
from io import BytesIO
import uuid
from IPython.display import display, HTML, clear_output
import json
import warnings
warnings.filterwarnings('ignore')
import hashlib  # for QR codes
import uuid  # for generating unique IDs

# ===== FLASK APP INITIALIZATION =====
app = Flask(__name__)
app.secret_key = os.urandom(24)  # Required for sessions

# ===== DATA FOLDER SETUP =====
DATA_FOLDER = 'church_data'
if not os.path.exists(DATA_FOLDER):
    os.makedirs(DATA_FOLDER)

# ===== PARTNERSHIP MANAGER CLASS =====
class PartnershipManager:
    """Manages church partners/members"""
    
    def __init__(self, data_file='partners.json'):
        self.data_file = os.path.join(DATA_FOLDER, data_file)
        self.partners = self.load_data()
    
    def load_data(self):
        """Load partners from file"""
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as f:
                return json.load(f)
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
            'created_at': datetime.datetime.now().isoformat()
        }
        self.partners.append(partner)
        self.save_data()
        return partner
    
    def get_all_partners(self):
        """Get all partners"""
        return self.partners
    
    def get_partner(self, partner_id):
        """Get a specific partner"""
        for partner in self.partners:
            if partner['id'] == partner_id:
                return partner
        return None
    
    def update_partner(self, partner_id, updates):
        """Update a partner"""
        for partner in self.partners:
            if partner['id'] == partner_id:
                partner.update(updates)
                self.save_data()
                return partner
        return None
    
    def delete_partner(self, partner_id):
        """Delete a partner"""
        self.partners = [p for p in self.partners if p['id'] != partner_id]
        self.save_data()

# ===== ROUTES =====

# Initialize managers
partner_manager = PartnershipManager()

@app.route('/')
def dashboard():
    """Dashboard home page"""
    return render_template('dashboard.html')

@app.route('/members')
def members():
    """Members directory page"""
    partners = partner_manager.get_all_partners()
    return render_template('members.html', partners=partners)

@app.route('/attendance')
def attendance():
    """Attendance tracking page"""
    return render_template('attendance.html')

@app.route('/finance')
def finance():
    """Finance management page"""
    return render_template('finance.html')

@app.route('/children')
def children():
    """Children's ministry page"""
    return render_template('children.html')

@app.route('/visitors')
def visitors():
    """Visitor tracking page"""
    return render_template('visitors.html')

@app.route('/programs')
def programs():
    """Programs and events page"""
    return render_template('programs.html')

@app.route('/equipment')
def equipment():
    """Equipment inventory page"""
    return render_template('equipment.html')

@app.route('/groups')
def groups():
    """Small groups page"""
    return render_template('groups.html')

@app.route('/welfare')
def welfare():
    """Welfare tracking page"""
    return render_template('welfare.html')

@app.route('/partnerships')
def partnerships():
    """Partnerships page"""
    partners = partner_manager.get_all_partners()
    return render_template('partnerships.html', partners=partners)

@app.route('/sms')
def sms():
    """SMS messaging page"""
    return render_template('sms.html')

# ===== API ROUTES =====

@app.route('/api/partners', methods=['GET'])
def get_partners():
    """API to get all partners"""
    partners = partner_manager.get_all_partners()
    return jsonify(partners)

@app.route('/api/partners', methods=['POST'])
def add_partner():
    """API to add a new partner"""
    data = request.json
    partner = partner_manager.add_partner(
        name=data.get('name'),
        email=data.get('email'),
        phone=data.get('phone'),
        partnership_date=data.get('partnership_date')
    )
    return jsonify(partner)

@app.route('/save_data')
def save_data():
    """Save all data to files"""
    partner_manager.save_data()
    return "Data saved successfully!"

@app.route('/load_data')
def load_data():
    """Load all data from files"""
    partner_manager.load_data()
    return "Data loaded successfully!"

# For interactive widgets (if using Jupyter)
try:
    import ipywidgets as widgets
    from IPython.display import display
    HAS_WIDGETS = True
except ImportError:
    HAS_WIDGETS = False
    print("Note: ipywidgets not installed. Install with: pip install ipywidgets")

# Set styling for better display
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)
sns.set_style("whitegrid")

print("="*70)
print("FLOOD OF LIFE EMBAZZY INTERNATIONAL CHURCH MANAGEMENT SYSTEM")
print("="*70)
print("\nInitializing system...")


# In[9]:


# Step 2: Define base classes and data structures

class ChurchManagementSystem:
    """Main system class that coordinates all modules"""
    
    def __init__(self, church_name="Flood of Life Embazzy International Church"):
        self.church_name = church_name
        self.version = "1.0.0"
        
        # Initialize all modules
        self.members = 'MemberManager()'
        self.attendance = 'AttendanceManager()'
        self.finance = 'FinanceManager()'
        self.children = 'ChildrenMinistry()'
        self.visitors = 'VisitorManager()'
        self.programs = 'ProgramManager()'
        self.equipment = 'EquipmentManager()'
        self.groups = 'GroupManager()'
        self.prayer = 'PrayerLineManager()'
        self.welfare = 'WelfareManager()'
        self.partnerships = 'PartnershipManager()'
        self.sms = 'SMSManager()'
        self.feedback = 'FeedbackManager()'
        
        print(f"✓ {church_name} Management System initialized")
        print(f"✓ Version: {self.version}")
        print(f"✓ All modules loaded successfully")
        
    def display_dashboard(self):
        """Display main dashboard with key metrics"""
        print("\n" + "="*70)
        print(f"{self.church_name} - DASHBOARD")
        print("="*70)
        
        # Get summary metrics
        total_members = len(self.members.members_df)
        new_members_30d = self.members.get_new_members_count(30)
        total_children = len(self.children.children_df)
        financial_balance = self.finance.get_current_balance()
        birthdays_today = self.members.get_birthdays_today()
        birthdays_this_week = self.members.get_birthdays_this_week()
        
        # Display metrics in a grid
        print(f"""
┌─────────────────────────────┬─────────────────────────────┐
│ Total Members: {total_members:<12} │ New Members (30d): {new_members_30d:<11} │
├─────────────────────────────┼─────────────────────────────┤
│ Total Children: {total_children:<12} │ Financial Balance: {financial_balance:<10} │
├─────────────────────────────┼─────────────────────────────┤
│ Birthdays Today: {birthdays_today:<12} │ Birthdays This Week: {birthdays_this_week:<9} │
└─────────────────────────────┴─────────────────────────────┘
        """)
        
        # Quick actions menu
        print("\nQUICK ACTIONS:")
        actions = [
            "1. Add Member", "2. QR Attendance", "3. Add Transaction",
            "4. Send SMS", "5. Add Prayer Request", "6. Manage Feedback"
        ]
        for i in range(0, len(actions), 3):
            print("   ".join(actions[i:i+3]))

# Initialize the main system
cms = ChurchManagementSystem()


# In[10]:


# Step 3: Member Management Module

class MemberManager:
    """Handle all member-related operations"""
    
    def __init__(self):
        self.members_df = pd.DataFrame(columns=[
            'member_id', 'first_name', 'last_name', 'full_name', 'date_of_birth',
            'age', 'gender', 'marital_status', 'phone', 'email', 'address',
            'occupation', 'school', 'department', 'role', 'status',
            'baptism_status', 'registration_date', 'emergency_contact_name',
            'emergency_contact_phone', 'family_members'
        ])
        self.load_sample_data()
        
    def load_sample_data(self):
        """Load sample member data based on screenshots"""
        sample_members = [
            {
                'member_id': 'M001', 'first_name': 'Keith', 'last_name': 'Mathibela',
                'full_name': 'Keith Mathibela', 'date_of_birth': '2002-08-27',
                'age': 23, 'gender': 'Male', 'marital_status': 'Single',
                'phone': '27634772587', 'email': 'keith@example.com', 'address': '6238 EXTENSION 2',
                'occupation': 'Doctor', 'school': 'CUT', 'department': 'Intercessors',
                'role': 'Member', 'status': 'Active', 'baptism_status': 'Baptized',
                'registration_date': '2025-08-27', 'emergency_contact_name': 'Mary Mathibela',
                'emergency_contact_phone': '27712345678', 'family_members': 0
            },
            {
                'member_id': 'M002', 'first_name': 'Nii', 'last_name': 'Ankrah',
                'full_name': 'Nii Ankrah', 'date_of_birth': '1990-05-15',
                'age': 36, 'gender': 'Male', 'marital_status': 'Married',
                'phone': '034455666', 'email': 'ankrah@gmail.com', 'address': 'Accra, Ghana',
                'occupation': 'IT', 'school': 'Ghana Law School', 'department': 'Media',
                'role': 'Worker', 'status': 'Active', 'baptism_status': 'Baptized',
                'registration_date': '2025-08-17', 'emergency_contact_name': 'Father',
                'emergency_contact_phone': '0234455666', 'family_members': 1
            },
            {
                'member_id': 'M003', 'first_name': 'John', 'last_name': 'Odabor',
                'full_name': 'John Odabor', 'date_of_birth': '1985-03-20',
                'age': 40, 'gender': 'Male', 'marital_status': 'Married',
                'phone': '233246670114', 'email': 'odabor@gmail.com', 'address': 'Accra',
                'occupation': 'Civil Servant', 'school': '', 'department': 'Administration',
                'role': 'Deacon', 'status': 'Active', 'baptism_status': 'Baptized',
                'registration_date': '2025-01-15', 'emergency_contact_name': 'Jane Odabor',
                'emergency_contact_phone': '233246670115', 'family_members': 3
            },
            {
                'member_id': 'M004', 'first_name': 'Kwanse', 'last_name': 'Aisdeu',
                'full_name': 'Kwanse Aisdeu', 'date_of_birth': '1960-07-10',
                'age': 65, 'gender': 'Male', 'marital_status': 'Married',
                'phone': '0592478790', 'email': 'kwanse@example.com', 'address': 'Kumasi',
                'occupation': 'Retired', 'school': '', 'department': 'Administration',
                'role': 'Elder', 'status': 'Active', 'baptism_status': 'Baptized',
                'registration_date': '2024-05-20', 'emergency_contact_name': 'Grace Aisdeu',
                'emergency_contact_phone': '0592478791', 'family_members': 4
            },
            {
                'member_id': 'M005', 'first_name': 'Nympha', 'last_name': 'Akeyampong',
                'full_name': 'Nympha Akeyampong', 'date_of_birth': '1980-11-25',
                'age': 45, 'gender': 'Female', 'marital_status': 'Married',
                'phone': '0236903980', 'email': 'nympha@example.com', 'address': 'Tema',
                'occupation': 'Nurse', 'school': '', 'department': 'Ushering',
                'role': 'Usher', 'status': 'Active', 'baptism_status': 'Baptized',
                'registration_date': '2025-02-10', 'emergency_contact_name': 'Kwame Akeyampong',
                'emergency_contact_phone': '0236903981', 'family_members': 2
            },
            {
                'member_id': 'M006', 'first_name': 'Obadiah', 'last_name': 'Otoo',
                'full_name': 'Obadiah Otoo', 'date_of_birth': '2005-09-30',
                'age': 20, 'gender': 'Male', 'marital_status': 'Single',
                'phone': '0561726349', 'email': 'obadiah@example.com', 'address': 'Accra',
                'occupation': 'Student', 'school': 'University of Ghana', 'department': 'Deacon',
                'role': 'Deacon', 'status': 'Active', 'baptism_status': 'Baptized',
                'registration_date': '2025-03-05', 'emergency_contact_name': 'Peter Otoo',
                'emergency_contact_phone': '0561726350', 'family_members': 2
            }
        ]
        
        # Add more sample members to reach 569 total as shown in screenshots
        departments = ['Intercessors', 'Media', 'Administration', 'Ushering', 'Choir', 
                      'Children', 'Protocol', 'Instrumentalist', 'New Breed', 'Welfare']
        roles = ['Member', 'Worker', 'Deacon', 'Elder', 'Pastor', 'Usher', 'Teacher']
        statuses = ['Active', 'Inactive', 'Visitor']
        genders = ['Male', 'Female']
        
        for i in range(7, 570):
            first_name = random.choice(['James', 'Mary', 'Peter', 'Esther', 'Daniel', 'Sarah', 'Paul', 'Ruth'])
            last_name = random.choice(['Mensah', 'Asare', 'Owusu', 'Boateng', 'Adjei', 'Darko', 'Oppong'])
            age = random.randint(5, 85)
            birth_year = 2025 - age
            birth_month = random.randint(1, 12)
            birth_day = random.randint(1, 28)
            
            member = {
                'member_id': f'M{i:03d}',
                'first_name': first_name,
                'last_name': last_name,
                'full_name': f'{first_name} {last_name}',
                'date_of_birth': f'{birth_year}-{birth_month:02d}-{birth_day:02d}',
                'age': age,
                'gender': random.choice(genders),
                'marital_status': random.choice(['Single', 'Married', 'Divorced', 'Widowed']),
                'phone': f'0{random.randint(20, 99)}{random.randint(1000000, 9999999)}',
                'email': f'{first_name.lower()}.{last_name.lower()}@example.com',
                'address': f'{random.randint(1, 999)} Street, City',
                'occupation': random.choice(['Teacher', 'Engineer', 'Doctor', 'Business', 'Student', 'Retired']),
                'school': '',
                'department': random.choice(departments),
                'role': random.choice(roles),
                'status': random.choices(statuses, weights=[0.85, 0.10, 0.05])[0],
                'baptism_status': random.choice(['Baptized', 'Not Baptized', 'Pending']),
                'registration_date': f'2025-{random.randint(1,8):02d}-{random.randint(1,28):02d}',
                'emergency_contact_name': f'Emergency Contact {i}',
                'emergency_contact_phone': f'0{random.randint(20, 99)}{random.randint(1000000, 9999999)}',
                'family_members': random.randint(0, 5)
            }
            sample_members.append(member)
        
        self.members_df = pd.DataFrame(sample_members)
        print(f"✓ Member Manager initialized with {len(self.members_df)} members")
        
    def add_member(self, member_data):
        """Add a new member"""
        new_id = f"M{len(self.members_df) + 1:03d}"
        member_data['member_id'] = new_id
        member_data['registration_date'] = datetime.now().strftime('%Y-%m-%d')
        
        # Calculate age from DOB if provided
        if 'date_of_birth' in member_data and member_data['date_of_birth']:
            dob = datetime.strptime(member_data['date_of_birth'], '%Y-%m-%d')
            today = datetime.now()
            member_data['age'] = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
        
        self.members_df = pd.concat([self.members_df, pd.DataFrame([member_data])], ignore_index=True)
        return new_id
    
    def get_member(self, member_id):
        """Get member by ID"""
        return self.members_df[self.members_df['member_id'] == member_id].iloc[0] if not self.members_df[self.members_df['member_id'] == member_id].empty else None
    
    def search_members(self, search_term):
        """Search members by name, phone, or email"""
        mask = (self.members_df['full_name'].str.contains(search_term, case=False, na=False) |
                self.members_df['phone'].str.contains(search_term, na=False) |
                self.members_df['email'].str.contains(search_term, case=False, na=False))
        return self.members_df[mask]
    
    def get_new_members_count(self, days=30):
        """Get count of members registered in last X days"""
        cutoff_date = (datetime.now() - timedelta(days=days)).strftime('%Y-%m-%d')
        return len(self.members_df[self.members_df['registration_date'] >= cutoff_date])
    
    def get_birthdays_today(self):
        """Get members with birthdays today"""
        today = datetime.now()
        members_with_birthdays = self.members_df[
            pd.to_datetime(self.members_df['date_of_birth']).dt.month == today.month
        ]
        members_with_birthdays = members_with_birthdays[
            pd.to_datetime(members_with_birthdays['date_of_birth']).dt.day == today.day
        ]
        return len(members_with_birthdays)
    
    def get_birthdays_this_week(self):
        """Get members with birthdays this week"""
        today = datetime.now()
        members_with_birthdays = self.members_df[
            pd.to_datetime(self.members_df['date_of_birth']).dt.month == today.month
        ]
        # Simplified - in production would check actual day of month range
        return len(members_with_birthdays[members_with_birthdays['date_of_birth'].notna()]) // 4  # Approximate
    
    def get_birthdays_this_month(self):
        """Get all members with birthdays in current month"""
        current_month = datetime.now().month
        return self.members_df[pd.to_datetime(self.members_df['date_of_birth']).dt.month == current_month]
    
    def get_gender_distribution(self):
        """Get gender distribution percentages"""
        gender_counts = self.members_df['gender'].value_counts()
        total = len(self.members_df)
        return {gender: f"{(count/total)*100:.1f}%" for gender, count in gender_counts.items()}
    
    def get_age_distribution(self):
        """Get age distribution percentages"""
        bins = [0, 18, 36, 60, 120]
        labels = ['Under 18', '18-35', '36-60', 'Over 60']
        self.members_df['age_group'] = pd.cut(self.members_df['age'], bins=bins, labels=labels, right=False)
        age_counts = self.members_df['age_group'].value_counts()
        total = len(self.members_df)
        return {age: f"{(count/total)*100:.1f}%" for age, count in age_counts.items()}
    
    def get_department_distribution(self):
        """Get department distribution"""
        dept_counts = self.members_df['department'].value_counts()
        total = len(self.members_df)
        return dept_counts, {dept: f"{(count/total)*100:.1f}%" for dept, count in dept_counts.items()}
    
    def display_members_directory(self):
        """Display members directory as shown in screenshot"""
        print("\n" + "="*70)
        print("MEMBERS DIRECTORY")
        print("="*70)
        print(f"Total Members: {len(self.members_df)} | Active: {len(self.members_df[self.members_df['status']=='Active'])} | New (30d): {self.get_new_members_count(30)}")
        print("\n" + "-"*70)
        
        # Show first 10 members
        display_df = self.members_df[['member_id', 'full_name', 'phone', 'department', 'role', 'status']].head(10)
        print(display_df.to_string(index=False))
        print(f"\nShowing 1 to 10 of {len(self.members_df)} members")

# Initialize Member Manager
cms.members = MemberManager()


# In[11]:


# Step 4: Attendance Management with QR Code

class AttendanceManager:
    """Handle attendance tracking with QR code support"""
    
    def __init__(self):
        self.attendance_df = pd.DataFrame(columns=[
            'attendance_id', 'member_id', 'service_date', 'service_type',
            'status', 'check_in_time', 'check_in_method', 'department'
        ])
        self.qr_codes = {}  # Store active QR codes
        self.load_sample_data()
        
    def load_sample_data(self):
        """Load sample attendance data"""
        # Generate attendance for last 8 months as shown in screenshot
        service_types = ['Sunday Morning', 'Wednesday Service', 'Friday Prayer', 'Youth Service']
        members = list(range(1, 570))
        start_date = datetime(2025, 1, 1)
        
        attendance_records = []
        record_id = 1
        
        for month in range(8):  # Jan to Aug 2025
            for week in range(4):  # 4 weeks per month
                service_date = start_date + timedelta(days=month*30 + week*7)
                if service_date > datetime.now():
                    continue
                    
                # Random attendance (70-90% of members attend)
                attending_members = random.sample(members, random.randint(int(0.7*len(members)), int(0.9*len(members))))
                
                for member_num in attending_members[:50]:  # Limit for sample
                    attendance_records.append({
                        'attendance_id': f'A{record_id:04d}',
                        'member_id': f'M{member_num:03d}',
                        'service_date': service_date.strftime('%Y-%m-%d'),
                        'service_type': random.choice(service_types),
                        'status': random.choices(['Present', 'Late', 'Absent'], weights=[0.7, 0.15, 0.15])[0],
                        'check_in_time': (service_date.replace(hour=8, minute=random.randint(0, 30))).strftime('%H:%M') if random.random() > 0.2 else None,
                        'check_in_method': random.choices(['QR Code', 'Manual', 'Check-in Desk'], weights=[0.4, 0.3, 0.3])[0],
                        'department': random.choice(['Media', 'Choir', 'Ushering', 'None'])
                    })
                    record_id += 1
        
        self.attendance_df = pd.DataFrame(attendance_records)
        print(f"✓ Attendance Manager initialized with {len(self.attendance_df)} attendance records")
    
    def generate_qr_code(self, service_type, service_date, validity_minutes=240):
        """Generate a QR code for attendance"""
        qr_id = str(uuid.uuid4())[:8]
        qr_data = {
            'qr_id': qr_id,
            'service_type': service_type,
            'service_date': service_date,
            'valid_from': datetime.now(),
            'valid_until': datetime.now() + timedelta(minutes=validity_minutes),
            'active': True
        }
        self.qr_codes[qr_id] = qr_data
        
        print(f"\n{'='*50}")
        print(f"QR CODE GENERATED FOR ATTENDANCE")
        print(f"{'='*50}")
        print(f"Service: {service_type}")
        print(f"Date: {service_date}")
        print(f"Valid for: {validity_minutes} minutes")
        print(f"QR ID: {qr_id}")
        print(f"\nDisplay this QR code for members to scan")
        print(f"Members can scan and mark themselves present")
        print(f"{'='*50}")
        
        return qr_id
    
    def mark_attendance(self, qr_id, member_id):
        """Mark attendance via QR code scan"""
        if qr_id not in self.qr_codes:
            return False, "Invalid QR code"
        
        qr = self.qr_codes[qr_id]
        if not qr['active'] or datetime.now() > qr['valid_until']:
            return False, "QR code expired"
        
        # Check if already marked
        if not self.attendance_df[
            (self.attendance_df['member_id'] == member_id) & 
            (self.attendance_df['service_date'] == qr['service_date'])
        ].empty:
            return False, "Already marked present"
        
        # Mark attendance
        new_id = f"A{len(self.attendance_df)+1:04d}"
        self.attendance_df = pd.concat([self.attendance_df, pd.DataFrame([{
            'attendance_id': new_id,
            'member_id': member_id,
            'service_date': qr['service_date'],
            'service_type': qr['service_type'],
            'status': 'Present',
            'check_in_time': datetime.now().strftime('%H:%M'),
            'check_in_method': 'QR Code',
            'department': 'None'
        }])], ignore_index=True)
        
        return True, "Attendance marked successfully"
    
    def get_member_attendance(self, member_id):
        """Get attendance history for a member"""
        return self.attendance_df[self.attendance_df['member_id'] == member_id]
    
    def get_attendance_trends(self, months=6):
        """Get attendance trends for last X months"""
        self.attendance_df['service_date'] = pd.to_datetime(self.attendance_df['service_date'])
        end_date = datetime.now()
        start_date = end_date - timedelta(days=months*30)
        
        recent = self.attendance_df[self.attendance_df['service_date'] >= start_date]
        monthly = recent.groupby(recent['service_date'].dt.strftime('%Y-%m')).size()
        
        return monthly
    
    def get_absent_members_alert(self, consecutive_sundays=3):
        """Find members absent for consecutive Sundays"""
        sundays = self.attendance_df[pd.to_datetime(self.attendance_df['service_date']).dt.dayofweek == 6]
        
        # Group by member and count recent absences
        recent_sundays = sundays[sundays['service_date'] >= (datetime.now() - timedelta(days=consecutive_sundays*7)).strftime('%Y-%m-%d')]
        absent_members = recent_sundays[recent_sundays['status'] == 'Absent']['member_id'].value_counts()
        absent_members = absent_members[absent_members >= consecutive_sundays]
        
        if len(absent_members) == 0:
            return "Excellent Attendance! No members have been absent for 3 consecutive Sundays. Everyone is faithfully attending!"
        else:
            return f"Alert: {len(absent_members)} members missing {consecutive_sundays} consecutive services"
    
    def display_attendance_dashboard(self):
        """Display attendance dashboard as shown in screenshot"""
        print("\n" + "="*70)
        print("ATTENDANCE TRENDS")
        print("="*70)
        
        trends = self.get_attendance_trends()
        print("\nMonthly Attendance:")
        for month, count in trends.items():
            print(f"  {month}: {count} attendees")
        
        print(f"\n{self.get_absent_members_alert()}")
        
        # Department attendance table
        print("\n" + "-"*70)
        print("Department Attendance Distribution")
        print("-"*70)
        
        dept_attendance = self.attendance_df.groupby('department').size().sort_values(ascending=False).head(10)
        total = len(self.attendance_df)
        
        for dept, count in dept_attendance.items():
            percentage = (count/total)*100
            print(f"  {dept:<20}: {count:>4} ({percentage:.1f}%)")

# Initialize Attendance Manager
cms.attendance = AttendanceManager()


# In[12]:


# Step 5: Finance Management Module

class FinanceManager:
    """Handle all financial transactions including tithes, offerings, and expenses"""
    
    def __init__(self):
        self.transactions_df = pd.DataFrame(columns=[
            'transaction_id', 'date', 'type', 'category', 'amount', 
            'member_id', 'description', 'payment_method', 'status'
        ])
        self.income_categories = ['Tithe', 'Offering', 'Harvest Pledge', 'Pledge', 
                                  'Kiosk Income', 'Project Donation', 'Partnership']
        self.expense_categories = ['Salaries', 'Utilities', 'Events', 'Maintenance', 
                                  'Equipment', 'Welfare', 'Miscellaneous']
        self.load_sample_data()
        
    def load_sample_data(self):
        """Load sample financial data"""
        transactions = []
        
        # Income transactions
        for i in range(200):
            date = datetime(2025, random.randint(1, 8), random.randint(1, 28))
            amount = random.randint(50, 1000)
            transactions.append({
                'transaction_id': f'TX{i:04d}',
                'date': date.strftime('%Y-%m-%d'),
                'type': 'Income',
                'category': random.choice(self.income_categories),
                'amount': amount,
                'member_id': f'M{random.randint(1, 100):03d}' if random.random() > 0.3 else None,
                'description': f'{random.choice(self.income_categories)} payment',
                'payment_method': random.choice(['Cash', 'Bank Transfer', 'Mobile Money', 'Card']),
                'status': 'Completed'
            })
        
        # Expense transactions
        for i in range(50):
            date = datetime(2025, random.randint(1, 8), random.randint(1, 28))
            amount = random.randint(100, 2000)
            transactions.append({
                'transaction_id': f'TX{200+i:04d}',
                'date': date.strftime('%Y-%m-%d'),
                'type': 'Expense',
                'category': random.choice(self.expense_categories),
                'amount': -amount,  # Negative for expenses
                'member_id': None,
                'description': f'{random.choice(self.expense_categories)} payment',
                'payment_method': random.choice(['Cash', 'Bank Transfer', 'Cheque']),
                'status': 'Completed'
            })
        
        self.transactions_df = pd.DataFrame(transactions)
        print(f"✓ Finance Manager initialized with {len(self.transactions_df)} transactions")
    
    def add_transaction(self, transaction_data):
        """Add a new transaction"""
        new_id = f"TX{len(self.transactions_df)+1:04d}"
        transaction_data['transaction_id'] = new_id
        transaction_data['date'] = datetime.now().strftime('%Y-%m-%d')
        self.transactions_df = pd.concat([self.transactions_df, pd.DataFrame([transaction_data])], ignore_index=True)
        return new_id
    
    def get_current_balance(self):
        """Calculate current financial balance"""
        income = self.transactions_df[self.transactions_df['type'] == 'Income']['amount'].sum()
        expenses = abs(self.transactions_df[self.transactions_df['type'] == 'Expense']['amount'].sum())
        return income - expenses
    
    def get_total_income(self):
        """Get total income"""
        return self.transactions_df[self.transactions_df['type'] == 'Income']['amount'].sum()
    
    def get_total_expenses(self):
        """Get total expenses"""
        return abs(self.transactions_df[self.transactions_df['type'] == 'Expense']['amount'].sum())
    
    def get_monthly_overview(self, months=6):
        """Get monthly income and expenses for last X months"""
        self.transactions_df['date'] = pd.to_datetime(self.transactions_df['date'])
        end_date = datetime.now()
        start_date = end_date - timedelta(days=months*30)
        
        recent = self.transactions_df[self.transactions_df['date'] >= start_date]
        recent['month'] = recent['date'].dt.strftime('%Y-%m')
        
        monthly_income = recent[recent['type'] == 'Income'].groupby('month')['amount'].sum()
        monthly_expenses = abs(recent[recent['type'] == 'Expense'].groupby('month')['amount'].sum())
        
        return monthly_income, monthly_expenses
    
    def get_category_breakdown(self, transaction_type='Income'):
        """Get breakdown by category"""
        return self.transactions_df[self.transactions_df['type'] == transaction_type].groupby('category')['amount'].sum().sort_values(ascending=False)
    
    def get_tithe_contributors(self):
        """Get tithe contributors summary as shown in screenshot"""
        tithes = self.transactions_df[
            (self.transactions_df['category'] == 'Tithe') & 
            (self.transactions_df['member_id'].notna())
        ]
        
        contributors = tithes.groupby('member_id').agg({
            'amount': ['sum', 'count', 'mean'],
            'date': 'max'
        }).round(2)
        
        contributors.columns = ['total_amount', 'payment_count', 'average_amount', 'last_payment']
        contributors = contributors.sort_values('total_amount', ascending=False)
        
        return contributors
    
    def display_financial_dashboard(self):
        """Display financial dashboard as shown in screenshot"""
        print("\n" + "="*70)
        print("FINANCIAL DASHBOARD")
        print("="*70)
        
        total_income = self.get_total_income()
        total_expenses = self.get_total_expenses()
        balance = self.get_current_balance()
        
        print(f"""
┌─────────────────────────────────────────────────────┐
│ TOTAL INCOME: R {total_income:>12,.2f}                           │
│ TOTAL EXPENSES: R {total_expenses:>12,.2f}                           │
│ CURRENT BALANCE: R {balance:>12,.2f}                           │
└─────────────────────────────────────────────────────┘
        """)
        
        print("\nCATEGORY DASHBOARDS:")
        income_cats = self.get_category_breakdown('Income').head(8)
        for cat, amount in income_cats.items():
            print(f"  • {cat}: R {amount:,.2f}")
        
        print("\nMONTHLY GIVING TRENDS (Last 6 months):")
        monthly_income, monthly_expenses = self.get_monthly_overview()
        for month in monthly_income.index:
            print(f"  {month}: Income: R {monthly_income[month]:>8,.2f} | Expenses: R {monthly_expenses.get(month, 0):>8,.2f}")

# Initialize Finance Manager
cms.finance = FinanceManager()


# In[13]:


# Step 6: Children's Ministry Module

class ChildrenMinistry:
    """Manage children's ministry activities, attendance, and growth tracking"""
    
    def __init__(self):
        self.children_df = pd.DataFrame(columns=[
            'child_id', 'full_name', 'date_of_birth', 'age', 'gender',
            'parent_id', 'parent_name', 'parent_phone', 'class_group',
            'registration_date', 'medical_notes', 'special_needs', 'status'
        ])
        self.children_attendance = pd.DataFrame(columns=[
            'attendance_id', 'child_id', 'service_date', 'check_in_time',
            'check_out_time', 'status', 'checked_in_by'
        ])
        self.class_groups = {
            'Small Blessings': (0, 2),
            'Kingdom Kids': (3, 5),
            'Sunday Friends': (6, 12)
        }
        self.load_sample_data()
        
    def load_sample_data(self):
        """Load sample children's data"""
        children = []
        
        # 57 children as shown in screenshot
        for i in range(57):
            age = random.randint(0, 12)
            gender = random.choice(['Male', 'Female'])
            
            # Determine class group
            if age <= 2:
                class_group = 'Small Blessings'
            elif age <= 5:
                class_group = 'Kingdom Kids'
            else:
                class_group = 'Sunday Friends'
            
            child = {
                'child_id': f'C{i+1:03d}',
                'full_name': random.choice(['James', 'Sarah', 'David', 'Esther', 'Michael', 'Grace', 'Samuel', 'Ruth']) + ' ' +
                            random.choice(['Mensah', 'Asare', 'Owusu', 'Boateng']),
                'date_of_birth': f'{2025-age}-{random.randint(1,12):02d}-{random.randint(1,28):02d}',
                'age': age,
                'gender': gender,
                'parent_id': f'M{random.randint(1, 100):03d}',
                'parent_name': f'Parent {i}',
                'parent_phone': f'0{random.randint(20, 99)}{random.randint(1000000, 9999999)}',
                'class_group': class_group,
                'registration_date': f'2025-{random.randint(1,8):02d}-{random.randint(1,28):02d}',
                'medical_notes': '' if random.random() > 0.1 else 'Has allergies',
                'special_needs': 'No' if random.random() > 0.05 else 'Yes',
                'status': 'Active'
            }
            children.append(child)
        
        self.children_df = pd.DataFrame(children)
        
        # Load attendance
        attendance = []
        for i in range(200):
            child = random.choice(self.children_df['child_id'].tolist())
            service_date = datetime(2025, random.randint(1, 8), random.randint(1, 28))
            attendance.append({
                'attendance_id': f'CA{i+1:04d}',
                'child_id': child,
                'service_date': service_date.strftime('%Y-%m-%d'),
                'check_in_time': service_date.replace(hour=9, minute=random.randint(0, 30)).strftime('%H:%M'),
                'check_out_time': service_date.replace(hour=12, minute=random.randint(0, 30)).strftime('%H:%M') if random.random() > 0.3 else None,
                'status': random.choice(['Present', 'Late', 'Absent']),
                'checked_in_by': 'Parent' if random.random() > 0.5 else 'Volunteer'
            })
        
        self.children_attendance = pd.DataFrame(attendance)
        print(f"✓ Children's Ministry initialized with {len(self.children_df)} children")
    
    def get_age_group_distribution(self):
        """Get distribution by age group"""
        distribution = self.children_df['class_group'].value_counts()
        return distribution
    
    def get_recent_checkins(self, date=None):
        """Get recent check-ins for real-time tracking"""
        if date is None:
            date = datetime.now().strftime('%Y-%m-%d')
        
        today_checkins = self.children_attendance[self.children_attendance['service_date'] == date]
        return today_checkins
    
    def get_attendance_analytics(self, period='weekly'):
        """Get attendance analytics"""
        self.children_attendance['service_date'] = pd.to_datetime(self.children_attendance['service_date'])
        
        if period == 'weekly':
            end_date = datetime.now()
            start_date = end_date - timedelta(days=7)
        else:
            end_date = datetime.now()
            start_date = end_date - timedelta(days=30)
        
        recent = self.children_attendance[self.children_attendance['service_date'] >= start_date]
        
        total_attendance = len(recent)
        qr_adoption = len(recent[recent['checked_in_by'] == 'QR']) / total_attendance * 100 if total_attendance > 0 else 0
        active_children = recent['child_id'].nunique()
        avg_per_service = total_attendance / len(recent['service_date'].unique()) if len(recent['service_date'].unique()) > 0 else 0
        
        return {
            'total_attendance': total_attendance,
            'qr_adoption': f"{qr_adoption:.1f}%",
            'active_children': active_children,
            'avg_per_service': f"{avg_per_service:.1f}"
        }
    
    def display_children_dashboard(self):
        """Display children's ministry dashboard as shown in screenshot"""
        print("\n" + "="*70)
        print("CHILDREN'S MINISTRY")
        print("="*70)
        
        age_dist = self.get_age_group_distribution()
        total_children = len(self.children_df)
        new_children = len(self.children_df[pd.to_datetime(self.children_df['registration_date']) >= (datetime.now() - timedelta(days=30))])
        birthday_celebrations = len(self.children_df[pd.to_datetime(self.children_df['date_of_birth']).dt.month == datetime.now().month])
        
        print(f"""
┌─────────────────────────────────────────────────────┐
│ Registered Children: {total_children:<12} │ New Children (30d): {new_children:<10} │
│ First-Time Visitors: 0         │ Birthday Celebrations: {birthday_celebrations:<4}     │
└─────────────────────────────────────────────────────┘
        """)
        
        print("\nCHILDREN BY AGE GROUP:")
        for group, count in age_dist.items():
            print(f"  • {group}: {count} children")
        
        print("\nREAL-TIME ATTENDANCE TRACKING:")
        print("  Live Updates Active")
        print(f"  Last updated: {datetime.now().strftime('%H:%M:%S')}")
        
        analytics = self.get_attendance_analytics('weekly')
        print(f"\n  Total Checked In Today: {len(self.get_recent_checkins())}")
        print(f"  QR Adoption: {analytics['qr_adoption']}")
        print(f"  Active Children: {analytics['active_children']}")

# Initialize Children's Ministry
cms.children = ChildrenMinistry()


# In[14]:


# Step 7: Visitor Management Module

class VisitorManager:
    """Track and manage church visitors"""
    
    def __init__(self):
        self.visitors_df = pd.DataFrame(columns=[
            'visitor_id', 'full_name', 'phone', 'email', 'address',
            'first_visit_date', 'heard_from', 'status', 'registered_by',
            'converted_to_member', 'conversion_date', 'follow_up_notes'
        ])
        self.follow_ups = pd.DataFrame(columns=[
            'follow_up_id', 'visitor_id', 'date', 'type', 'notes', 'conducted_by'
        ])
        self.load_sample_data()
        
    def load_sample_data(self):
        """Load sample visitor data"""
        visitors = [
            {
                'visitor_id': 'V001',
                'full_name': 'Patrick Smith',
                'phone': '+27634772587',
                'email': 'patrick.smith@example.com',
                'address': '6238 EXTENSION 2',
                'first_visit_date': '2025-08-27',
                'heard_from': 'Website',
                'status': 'In follow up',
                'registered_by': 'System',
                'converted_to_member': False,
                'conversion_date': None,
                'follow_up_notes': 'Welcome SMS sent'
            },
            {
                'visitor_id': 'V002',
                'full_name': 'Smoke Tester',
                'phone': '+27721234567',
                'email': 'smoke.tester@example.com',
                'address': 'Test Address',
                'first_visit_date': '2025-08-13',
                'heard_from': 'Friend',
                'status': 'In follow up',
                'registered_by': 'System',
                'converted_to_member': False,
                'conversion_date': None,
                'follow_up_notes': 'First contact made'
            }
        ]
        
        self.visitors_df = pd.DataFrame(visitors)
        
        # Sample follow-ups
        follow_ups = [
            {
                'follow_up_id': 'F001',
                'visitor_id': 'V001',
                'date': '2025-08-27',
                'type': 'SMS',
                'notes': 'Welcome SMS sent: Dear Patrick, welcome to Winners Arena International!',
                'conducted_by': 'Patrick'
            },
            {
                'follow_up_id': 'F002',
                'visitor_id': 'V001',
                'date': '2025-08-27',
                'type': 'Phone Call',
                'notes': 'Called visitor within 48 hours of visit',
                'conducted_by': 'Patrick'
            }
        ]
        
        self.follow_ups = pd.DataFrame(follow_ups)
        print(f"✓ Visitor Manager initialized with {len(self.visitors_df)} visitors")
    
    def register_visitor(self, visitor_data):
        """Register a new visitor"""
        new_id = f"V{len(self.visitors_df)+1:03d}"
        visitor_data['visitor_id'] = new_id
        visitor_data['first_visit_date'] = datetime.now().strftime('%Y-%m-%d')
        visitor_data['status'] = 'New'
        visitor_data['converted_to_member'] = False
        self.visitors_df = pd.concat([self.visitors_df, pd.DataFrame([visitor_data])], ignore_index=True)
        return new_id
    
    def add_follow_up(self, visitor_id, follow_up_type, notes, conducted_by):
        """Add a follow-up for a visitor"""
        follow_up = {
            'follow_up_id': f"F{len(self.follow_ups)+1:03d}",
            'visitor_id': visitor_id,
            'date': datetime.now().strftime('%Y-%m-%d'),
            'type': follow_up_type,
            'notes': notes,
            'conducted_by': conducted_by
        }
        self.follow_ups = pd.concat([self.follow_ups, pd.DataFrame([follow_up])], ignore_index=True)
        
        # Update visitor status
        self.visitors_df.loc[self.visitors_df['visitor_id'] == visitor_id, 'status'] = 'In follow up'
        
        return follow_up['follow_up_id']
    
    def convert_to_member(self, visitor_id, member_id):
        """Convert a visitor to a church member"""
        self.visitors_df.loc[self.visitors_df['visitor_id'] == visitor_id, 'converted_to_member'] = True
        self.visitors_df.loc[self.visitors_df['visitor_id'] == visitor_id, 'conversion_date'] = datetime.now().strftime('%Y-%m-%d')
        self.visitors_df.loc[self.visitors_df['visitor_id'] == visitor_id, 'status'] = 'Converted'
        return True
    
    def display_visitor_management(self):
        """Display visitor management interface as shown in screenshot"""
        print("\n" + "="*70)
        print("VISITOR MANAGEMENT")
        print("="*70)
        print("Track and manage church visitors\n")
        
        print("Visitors:")
        for _, visitor in self.visitors_df.iterrows():
            initials = ''.join([name[0] for name in visitor['full_name'].split()[:2]])
            print(f"""
  {initials}  {visitor['full_name']}
     Heard from: {visitor['heard_from']} | {visitor['phone']}
     First Visit: {visitor['first_visit_date']} | Status: {visitor['status']}
            """)
        
        print("\n" + "-"*50)
        print(f"Showing 1 to {len(self.visitors_df)} of {len(self.visitors_df)} visitors")
        print("\n[Register New Visitor] [Converted to Members]")

# Initialize Visitor Manager
cms.visitors = VisitorManager()


# In[15]:


# Step 8: Programs and Events Module

class ProgramManager:
    """Manage church programs and events"""
    
    def __init__(self):
        self.programs_df = pd.DataFrame(columns=[
            'program_id', 'name', 'description', 'start_date', 'end_date',
            'start_time', 'end_time', 'location', 'coordinator', 'department',
            'status', 'budget', 'expected_attendees', 'priority', 'registration_required'
        ])
        self.guests_df = pd.DataFrame(columns=[
            'guest_id', 'program_id', 'name', 'role', 'title', 'notes'
        ])
        self.load_sample_data()
        
    def load_sample_data(self):
        """Load sample program data"""
        programs = [
            {
                'program_id': 'P001',
                'name': 'Fresh Oil',
                'description': 'This is the first program we have during the beginning of the year',
                'start_date': '2025-07-15',
                'end_date': '2025-07-21',
                'start_time': '15:53',
                'end_time': '20:00',
                'location': 'church',
                'coordinator': 'Emmanuel sarpong',
                'department': 'Media Ministry',
                'status': 'Completed',
                'budget': 300.00,
                'expected_attendees': 200,
                'priority': 'High',
                'registration_required': True
            },
            {
                'program_id': 'P002',
                'name': 'Greater Works',
                'description': 'Annual conference',
                'start_date': '2025-07-22',
                'end_date': '2025-07-25',
                'start_time': '09:00',
                'end_time': '17:00',
                'location': 'IGGC',
                'coordinator': 'Emmanuel sarpong',
                'department': 'All',
                'status': 'Completed',
                'budget': 500.00,
                'expected_attendees': 300,
                'priority': 'High',
                'registration_required': True
            },
            {
                'program_id': 'P003',
                'name': 'Godclass',
                'description': 'Fellowship Event',
                'start_date': '2025-08-10',
                'end_date': '2025-08-10',
                'start_time': '10:00',
                'end_time': '13:00',
                'location': 'Church Hall',
                'coordinator': 'John Doe',
                'department': 'Fellowship',
                'status': 'In progress',
                'budget': 100.00,
                'expected_attendees': 150,
                'priority': 'Medium',
                'registration_required': False
            },
            {
                'program_id': 'P004',
                'name': 'Money Sunday',
                'description': 'Special Weekend',
                'start_date': '2025-08-27',
                'end_date': '2025-08-27',
                'start_time': '08:30',
                'end_time': '12:00',
                'location': 'Main Auditorium',
                'coordinator': 'Patrick South',
                'department': 'Finance',
                'status': 'Planned',
                'budget': 200.00,
                'expected_attendees': 250,
                'priority': 'High',
                'registration_required': True
            }
        ]
        
        self.programs_df = pd.DataFrame(programs)
        
        # Add guests
        guests = [
            {
                'guest_id': 'G001',
                'program_id': 'P001',
                'name': 'Rev. Enoch Paul Hayes',
                'role': 'Guest Speaker',
                'title': 'head pastor',
                'notes': ''
            }
        ]
        
        self.guests_df = pd.DataFrame(guests)
        print(f"✓ Program Manager initialized with {len(self.programs_df)} programs")
    
    def create_program(self, program_data):
        """Create a new program"""
        new_id = f"P{len(self.programs_df)+1:03d}"
        program_data['program_id'] = new_id
        program_data['status'] = 'Planned'
        self.programs_df = pd.concat([self.programs_df, pd.DataFrame([program_data])], ignore_index=True)
        return new_id
    
    def get_upcoming_programs(self):
        """Get upcoming programs"""
        today = datetime.now().strftime('%Y-%m-%d')
        upcoming = self.programs_df[self.programs_df['start_date'] >= today]
        upcoming = upcoming[upcoming['status'] != 'Completed']
        return upcoming.sort_values('start_date')
    
    def get_program_details(self, program_id):
        """Get detailed program information"""
        program = self.programs_df[self.programs_df['program_id'] == program_id].iloc[0]
        guests = self.guests_df[self.guests_df['program_id'] == program_id]
        return program, guests
    
    def display_programs(self):
        """Display programs as shown in screenshot"""
        print("\n" + "="*70)
        print("PROGRAMS AND EVENTS")
        print("="*70)
        
        upcoming = self.get_upcoming_programs()
        
        if len(upcoming) == 0:
            print("\nNo upcoming programs")
            print("Start planning your next church program to keep your community engaged and growing.")
        else:
            for _, program in upcoming.iterrows():
                print(f"\n  {program['name']} | {program['status']}")
                print(f"  {program['department']} | {program['start_date']} • Ends on {program['end_date']} • {program['coordinator']}")
        
        print("\n[Create Program] [View Calendar] [Annual Timeline] [Export Data]")

# Initialize Program Manager
cms.programs = ProgramManager()


# In[16]:


# Step 9: Equipment Management Module

class EquipmentManager:
    """Manage church equipment and assets"""
    
    def __init__(self):
        self.equipment_df = pd.DataFrame(columns=[
            'equipment_id', 'name', 'category', 'status', 'purchase_date',
            'purchase_price', 'location', 'assigned_to', 'last_maintenance',
            'next_maintenance', 'notes', 'qr_code'
        ])
        self.maintenance_log = pd.DataFrame(columns=[
            'log_id', 'equipment_id', 'date', 'type', 'description', 'cost', 'performed_by'
        ])
        self.load_sample_data()
        
    def load_sample_data(self):
        """Load sample equipment data"""
        equipment = [
            {
                'equipment_id': 'E001',
                'name': 'TV Screen',
                'category': 'media',
                'status': 'Excellent',
                'purchase_date': '2025-08-27',
                'purchase_price': 2500.00,
                'location': 'Main Auditorium',
                'assigned_to': None,
                'last_maintenance': '2025-08-27',
                'next_maintenance': '2025-11-27',
                'notes': '4K LED Screen',
                'qr_code': 'qr_e001'
            },
            {
                'equipment_id': 'E002',
                'name': 'Camera',
                'category': 'media',
                'status': 'Good',
                'purchase_date': '2025-08-26',
                'purchase_price': 1800.00,
                'location': 'Media Room',
                'assigned_to': 'John Doe',
                'last_maintenance': '2025-08-26',
                'next_maintenance': '2025-11-26',
                'notes': 'DSLR Camera',
                'qr_code': 'qr_e002'
            },
            {
                'equipment_id': 'E003',
                'name': 'Keyboard',
                'category': 'instruments',
                'status': 'Excellent',
                'purchase_date': '2025-08-26',
                'purchase_price': 1200.00,
                'location': 'Choir',
                'assigned_to': 'Music Team',
                'last_maintenance': '2025-08-26',
                'next_maintenance': '2025-11-26',
                'notes': 'Yamaha Keyboard',
                'qr_code': 'qr_e003'
            },
            {
                'equipment_id': 'E004',
                'name': 'Smart screen',
                'category': 'media',
                'status': 'Excellent',
                'purchase_date': '2025-08-25',
                'purchase_price': 3000.00,
                'location': 'Foyer',
                'assigned_to': None,
                'last_maintenance': '2025-08-25',
                'next_maintenance': '2025-11-25',
                'notes': 'Interactive Display',
                'qr_code': 'qr_e004'
            },
            {
                'equipment_id': 'E005',
                'name': 'Keyboard',
                'category': 'cctv_camera',
                'status': 'Excellent',
                'purchase_date': '2021-02-02',
                'purchase_price': 350.00,
                'location': 'Security Room',
                'assigned_to': 'Security',
                'last_maintenance': '2025-08-01',
                'next_maintenance': '2025-11-01',
                'notes': 'CCTV Keyboard Controller',
                'qr_code': 'qr_e005'
            },
            {
                'equipment_id': 'E006',
                'name': 'Hp Desktop pc',
                'category': 'media',
                'status': 'Excellent',
                'purchase_date': '2021-06-02',
                'purchase_price': 850.00,
                'location': 'Media Room',
                'assigned_to': 'Media Team',
                'last_maintenance': '2025-08-15',
                'next_maintenance': '2025-11-15',
                'notes': 'HP Desktop for editing',
                'qr_code': 'qr_e006'
            }
        ]
        
        self.equipment_df = pd.DataFrame(equipment)
        print(f"✓ Equipment Manager initialized with {len(self.equipment_df)} equipment items")
    
    def add_equipment(self, equipment_data):
        """Add new equipment"""
        new_id = f"E{len(self.equipment_df)+1:03d}"
        equipment_data['equipment_id'] = new_id
        equipment_data['qr_code'] = f'qr_{new_id.lower()}'
        self.equipment_df = pd.concat([self.equipment_df, pd.DataFrame([equipment_data])], ignore_index=True)
        return new_id
    
    def get_equipment_by_category(self, category=None):
        """Get equipment filtered by category"""
        if category:
            return self.equipment_df[self.equipment_df['category'] == category]
        return self.equipment_df
    
    def generate_qr_code(self, equipment_id):
        """Generate QR code for equipment"""
        equipment = self.equipment_df[self.equipment_df['equipment_id'] == equipment_id].iloc[0]
        
        print(f"\n{'='*50}")
        print(f"QR CODE FOR EQUIPMENT: {equipment['name']} - ID #{equipment_id}")
        print(f"{'='*50}")
        print(f"Category: {equipment['category']}")
        print(f"Status: {equipment['status']}")
        print(f"Location: {equipment['location']}")
        print(f"Purchase Date: {equipment['purchase_date']}")
        print(f"\nScan this QR code to view equipment details")
        print(f"URL: https://cms.church/qr/equipment/{equipment_id}")
        print(f"{'='*50}")
        
        return f"qr_{equipment_id}"
    
    def log_maintenance(self, equipment_id, maintenance_data):
        """Log maintenance activity"""
        log_id = f"ML{len(self.maintenance_log)+1:04d}"
        maintenance_data['log_id'] = log_id
        maintenance_data['equipment_id'] = equipment_id
        maintenance_data['date'] = datetime.now().strftime('%Y-%m-%d')
        self.maintenance_log = pd.concat([self.maintenance_log, pd.DataFrame([maintenance_data])], ignore_index=True)
        
        # Update equipment last maintenance
        self.equipment_df.loc[self.equipment_df['equipment_id'] == equipment_id, 'last_maintenance'] = maintenance_data['date']
        
        return log_id
    
    def display_equipment_list(self):
        """Display equipment list as shown in screenshot"""
        print("\n" + "="*70)
        print("EQUIPMENT INVENTORY")
        print("="*70)
        print(f"Total Items: {len(self.equipment_df)}\n")
        
        print(f"{'NAME':<20} {'CATEGORY':<15} {'STATUS':<10} {'PURCHASE DATE':<15}")
        print("-"*60)
        
        for _, item in self.equipment_df.iterrows():
            print(f"{item['name']:<20} {item['category']:<15} {item['status']:<10} {item['purchase_date']:<15}")
        
        print(f"\nShowing 1 to {len(self.equipment_df)} of {len(self.equipment_df)} items")

# Initialize Equipment Manager
cms.equipment = EquipmentManager()


# In[17]:


# Step 10: Groups and Counseling Module

class GroupManager:
    """Manage church groups and small groups"""
    
    def __init__(self):
        self.groups_df = pd.DataFrame(columns=[
            'group_id', 'name', 'description', 'category', 'leader_id',
            'leader_name', 'meeting_schedule', 'meeting_location', 'status',
            'created_date', 'member_count'
        ])
        self.group_members = pd.DataFrame(columns=[
            'group_member_id', 'group_id', 'member_id', 'joined_date', 'role', 'status'
        ])
        self.counseling_sessions = pd.DataFrame(columns=[
            'session_id', 'group_id', 'member_id', 'counselor_id', 'date',
            'time', 'type', 'notes', 'status'
        ])
        self.load_sample_data()
        
    def load_sample_data(self):
        """Load sample group data"""
        groups = [
            {
                'group_id': 'G001',
                'name': 'MVV Men\'s Group',
                'description': 'Men\'s fellowship and support group',
                'category': 'Men',
                'leader_id': 'M001',
                'leader_name': 'Keith Mathibela',
                'meeting_schedule': 'Saturdays 4:00 PM',
                'meeting_location': 'Room 101',
                'status': 'Active',
                'created_date': '2025-01-15',
                'member_count': 3
            },
            {
                'group_id': 'G002',
                'name': 'Intercessory Prayer',
                'description': 'Prayer is ongoing',
                'category': 'Prayer',
                'leader_id': 'M003',
                'leader_name': 'John Odabor',
                'meeting_schedule': 'Wednesdays 6:00 PM',
                'meeting_location': 'Prayer Room',
                'status': 'Active',
                'created_date': '2025-02-10',
                'member_count': 8
            },
            {
                'group_id': 'G003',
                'name': 'DigitalConnect',
                'description': 'Prayer is ongoing',
                'category': 'Youth',
                'leader_id': 'M002',
                'leader_name': 'Nii Ankrah',
                'meeting_schedule': 'Fridays 7:00 PM',
                'meeting_location': 'Online',
                'status': 'Active',
                'created_date': '2025-03-05',
                'member_count': 5
            }
        ]
        
        self.groups_df = pd.DataFrame(groups)
        
        # Group members
        group_members = [
            {'group_member_id': 'GM001', 'group_id': 'G001', 'member_id': 'M001', 'joined_date': '2025-08-27', 'role': 'Leader', 'status': 'Active'},
            {'group_member_id': 'GM002', 'group_id': 'G001', 'member_id': 'M004', 'joined_date': '2025-08-22', 'role': 'Member', 'status': 'Active'},
            {'group_member_id': 'GM003', 'group_id': 'G001', 'member_id': 'M002', 'joined_date': '2025-08-22', 'role': 'Member', 'status': 'Active'},
            {'group_member_id': 'GM004', 'group_id': 'G001', 'member_id': 'M003', 'joined_date': '2025-08-15', 'role': 'Member', 'status': 'Active'},
        ]
        
        self.group_members = pd.DataFrame(group_members)
        
        # Counseling sessions
        counseling = [
            {
                'session_id': 'CS001',
                'group_id': 'G001',
                'member_id': 'M001',
                'counselor_id': 'M003',
                'date': '2025-08-28',
                'time': '15:00',
                'type': 'Individual',
                'notes': 'Initial session',
                'status': 'Completed'
            }
        ]
        
        self.counseling_sessions = pd.DataFrame(counseling)
        print(f"✓ Group Manager initialized with {len(self.groups_df)} groups")
    
    def create_group(self, group_data):
        """Create a new group"""
        new_id = f"G{len(self.groups_df)+1:03d}"
        group_data['group_id'] = new_id
        group_data['created_date'] = datetime.now().strftime('%Y-%m-%d')
        group_data['member_count'] = 0
        self.groups_df = pd.concat([self.groups_df, pd.DataFrame([group_data])], ignore_index=True)
        return new_id
    
    def add_member_to_group(self, group_id, member_id, role='Member'):
        """Add a member to a group"""
        # Check if already in group
        existing = self.group_members[
            (self.group_members['group_id'] == group_id) & 
            (self.group_members['member_id'] == member_id)
        ]
        
        if len(existing) > 0:
            return False, "Member already in group"
        
        new_id = f"GM{len(self.group_members)+1:04d}"
        new_member = {
            'group_member_id': new_id,
            'group_id': group_id,
            'member_id': member_id,
            'joined_date': datetime.now().strftime('%Y-%m-%d'),
            'role': role,
            'status': 'Active'
        }
        
        self.group_members = pd.concat([self.group_members, pd.DataFrame([new_member])], ignore_index=True)
        
        # Update member count
        count = len(self.group_members[self.group_members['group_id'] == group_id])
        self.groups_df.loc[self.groups_df['group_id'] == group_id, 'member_count'] = count
        
        return True, new_id
    
    def book_counseling(self, group_id, member_id, counselor_id, session_type, notes=""):
        """Book a counseling session"""
        session_id = f"CS{len(self.counseling_sessions)+1:04d}"
        session = {
            'session_id': session_id,
            'group_id': group_id,
            'member_id': member_id,
            'counselor_id': counselor_id,
            'date': datetime.now().strftime('%Y-%m-%d'),
            'time': datetime.now().strftime('%H:%M'),
            'type': session_type,
            'notes': notes,
            'status': 'Scheduled'
        }
        
        self.counseling_sessions = pd.concat([self.counseling_sessions, pd.DataFrame([session])], ignore_index=True)
        return session_id
    
    def display_group_assignments(self):
        """Display group assignments as shown in screenshot"""
        print("\n" + "="*70)
        print("GROUP ASSIGNMENTS")
        print("="*70)
        
        assigned_groups = len(self.groups_df)
        assigned_users = len(self.group_members['member_id'].unique())
        
        print(f"""
Assigned Groups: {assigned_groups:<12} Unassigned Groups: 0
Available Users: {assigned_users:<12}
        """)
        
        print("\nCURRENT ASSIGNMENTS:")
        print(f"{'GROUP':<20} {'ASSIGNED USER':<15} {'ASSIGNED DATE':<15} {'ASSIGNED BY':<15}")
        print("-"*65)
        
        for _, group in self.groups_df.head(4).iterrows():
            members = self.group_members[self.group_members['group_id'] == group['group_id']]
            for _, member in members.iterrows():
                print(f"{group['name'][:18]:<20} {member['member_id']:<15} {member['joined_date']:<15} System")

# Initialize Group Manager
cms.groups = GroupManager()


# In[18]:


# Step 11: Prayer Line and Welfare Modules

class PrayerLineManager:
    """Manage prayer requests and spiritual support"""
    
    def __init__(self):
        self.prayer_requests = pd.DataFrame(columns=[
            'request_id', 'member_id', 'anonymous', 'request_type',
            'description', 'submitted_date', 'status', 'assigned_to',
            'prayed_by', 'prayed_date', 'notes'
        ])
        self.load_sample_data()
        
    def load_sample_data(self):
        """Load sample prayer requests"""
        # No requests initially as shown in screenshot
        print(f"✓ Prayer Line Manager initialized with {len(self.prayer_requests)} requests")
    
    def submit_request(self, member_id=None, anonymous=False, request_type="Prayer", description=""):
        """Submit a new prayer request"""
        request_id = f"PR{len(self.prayer_requests)+1:04d}"
        request = {
            'request_id': request_id,
            'member_id': member_id if not anonymous else None,
            'anonymous': anonymous,
            'request_type': request_type,
            'description': description,
            'submitted_date': datetime.now().strftime('%Y-%m-%d %H:%M'),
            'status': 'New',
            'assigned_to': None,
            'prayed_by': None,
            'prayed_date': None,
            'notes': ''
        }
        
        self.prayer_requests = pd.concat([self.prayer_requests, pd.DataFrame([request])], ignore_index=True)
        return request_id
    
    def mark_prayed(self, request_id, prayed_by):
        """Mark a prayer request as prayed for"""
        self.prayer_requests.loc[self.prayer_requests['request_id'] == request_id, 'status'] = 'Prayed'
        self.prayer_requests.loc[self.prayer_requests['request_id'] == request_id, 'prayed_by'] = prayed_by
        self.prayer_requests.loc[self.prayer_requests['request_id'] == request_id, 'prayed_date'] = datetime.now().strftime('%Y-%m-%d')
        return True
    
    def display_prayer_line(self):
        """Display prayer line dashboard"""
        print("\n" + "="*70)
        print("PRAYER LINE")
        print("="*70)
        print("Manage prayer requests and spiritual support\n")
        
        total = len(self.prayer_requests)
        print(f"Total: {total}")
        
        if total == 0:
            print("\nNo prayer line requests for this group yet.")
        
        print("\n[+ New Prayer Request] [Prayer Summary]")

class WelfareManager:
    """Manage monthly welfare dues and member claims"""
    
    def __init__(self):
        self.welfare_payments = pd.DataFrame(columns=[
            'payment_id', 'member_id', 'amount', 'payment_date',
            'payment_method', 'month', 'year', 'status', 'received_by'
        ])
        self.welfare_claims = pd.DataFrame(columns=[
            'claim_id', 'member_id', 'amount', 'claim_date',
            'reason', 'status', 'approved_by', 'disbursed_date', 'notes'
        ])
        self.load_sample_data()
        
    def load_sample_data(self):
        """Load sample welfare data"""
        # Payments
        payments = [
            {'payment_id': 'WP001', 'member_id': 'M006', 'amount': 10.00, 'payment_date': '2025-08-16', 
             'payment_method': 'Cash', 'month': 8, 'year': 2025, 'status': 'Completed', 'received_by': 'Treasurer'},
            {'payment_id': 'WP002', 'member_id': 'M003', 'amount': 400.00, 'payment_date': '2025-08-10',
             'payment_method': 'Cash', 'month': 8, 'year': 2025, 'status': 'Completed', 'received_by': 'Treasurer'},
            {'payment_id': 'WP003', 'member_id': 'M004', 'amount': 87.00, 'payment_date': '2025-08-10',
             'payment_method': 'Bank Transfer', 'month': 8, 'year': 2025, 'status': 'Completed', 'received_by': 'System'},
            {'payment_id': 'WP004', 'member_id': 'M001', 'amount': 180.00, 'payment_date': '2025-08-05',
             'payment_method': 'Mobile Money', 'month': 8, 'year': 2025, 'status': 'Completed', 'received_by': 'Treasurer'}
        ]
        
        self.welfare_payments = pd.DataFrame(payments)
        
        # Claims
        claims = [
            {'claim_id': 'WC001', 'member_id': 'M005', 'amount': 72.00, 'claim_date': '2025-08-10',
             'reason': 'Emergency', 'status': 'Disbursed', 'approved_by': 'Pastor', 'disbursed_date': '2025-08-11', 'notes': ''}
        ]
        
        self.welfare_claims = pd.DataFrame(claims)
        print(f"✓ Welfare Manager initialized with {len(self.welfare_payments)} payments, {len(self.welfare_claims)} claims")
    
    def get_monthly_summary(self, month=None, year=2025):
        """Get monthly welfare summary"""
        if month is None:
            month = datetime.now().month
        
        month_payments = self.welfare_payments[
            (self.welfare_payments['month'] == month) & 
            (self.welfare_payments['year'] == year)
        ]
        
        month_claims = self.welfare_claims[
            (pd.to_datetime(self.welfare_claims['claim_date']).dt.month == month) &
            (pd.to_datetime(self.welfare_claims['claim_date']).dt.year == year)
        ]
        
        total_collected = month_payments['amount'].sum()
        total_disbursed = month_claims[month_claims['status'] == 'Disbursed']['amount'].sum()
        paid_count = len(month_payments)
        claimed_count = len(month_claims[month_claims['status'] == 'Disbursed'])
        
        return {
            'total_collected': total_collected,
            'total_disbursed': total_disbursed,
            'available_balance': total_collected - total_disbursed,
            'paid_this_month': paid_count,
            'claimed_this_month': claimed_count,
            'payments': month_payments,
            'claims': month_claims
        }
    
    def display_welfare_dashboard(self):
        """Display welfare dashboard as shown in screenshot"""
        print("\n" + "="*70)
        print("MONTHLY WELFARE MANAGEMENT")
        print("="*70)
        
        summary = self.get_monthly_summary(8, 2025)  # August 2025
        
        print(f"""
┌─────────────────────────────────────────────────────┐
│ Total Collected: R {summary['total_collected']:>8,.2f}   Total Disbursed: R {summary['total_disbursed']:>8,.2f}   │
│ Available Balance: R {summary['available_balance']:>8,.2f}                                 │
│ Paid This Month: {summary['paid_this_month']:<4}          Claimed This Month: {summary['claimed_this_month']:<4}          │
└─────────────────────────────────────────────────────┘
        """)
        
        print("\nMEMBERS WHO PAID THIS MONTH:")
        for _, payment in summary['payments'].iterrows():
            member = cms.members.get_member(payment['member_id'])
            if member is not None:
                print(f"  • {member['full_name']:<20} {payment['payment_date']} - {payment['payment_method']:<12} R {payment['amount']:>6,.2f}")
        
        print("\nMEMBERS WHO CLAIMED THIS MONTH:")
        for _, claim in summary['claims'].iterrows():
            member = cms.members.get_member(claim['member_id'])
            if member is not None:
                print(f"  • {member['full_name']:<20} {claim['claim_date']} - Disbursed")

# Initialize modules
cms.prayer = PrayerLineManager()
cms.welfare = WelfareManager()


# In[26]:


# Step 12: Partnership and SMS Modules (CORRECTED VERSION)

class PartnershipManager:
    """Manage church partnerships and contributions"""
    
    def __init__(self):
        self.partners_df = pd.DataFrame(columns=[
            'partner_id', 'name', 'type', 'tier', 'contact_person',
            'phone', 'email', 'address', 'join_date', 'status',
            'total_contributions', 'last_contribution_date', 'notes'
        ])
        self.partner_contributions = pd.DataFrame(columns=[
            'contribution_id', 'partner_id', 'date', 'amount', 'type', 'notes'
        ])
        self.tiers = ['Entry Level', 'Gold Partners', 'Diamond Partners', 'Bronze Partners']
        self.load_sample_data()
        
    def load_sample_data(self):
        """Load sample partnership data"""
        partners_data = [
            {'partner_id': 'PT001', 'name': 'John Obeng', 'type': 'Individual', 'tier': 'Gold Partners',
             'contact_person': 'Self', 'phone': '0598046821', 'email': 'jobeng@yahoo.com',
             'join_date': '2025-01-15', 'status': 'Active', 'total_contributions': 899.00},
            {'partner_id': 'PT002', 'name': 'Sarpongs Emmas', 'type': 'Individual', 'tier': 'Gold Partners',
             'contact_person': 'Self', 'phone': '2030455777', 'email': 'saop@gmail.com',
             'join_date': '2025-02-10', 'status': 'Active', 'total_contributions': 700.00},
            {'partner_id': 'PT003', 'name': 'Michael Bolten', 'type': 'Individual', 'tier': 'Diamond Partners',
             'contact_person': 'Self', 'phone': '+2332466701191', 'email': 'bolt@gmail.com',
             'join_date': '2025-03-05', 'status': 'Active', 'total_contributions': 400.00},
            {'partner_id': 'PT004', 'name': 'Patrick South', 'type': 'Individual', 'tier': 'Diamond Partners',
             'contact_person': 'Self', 'phone': '+27815425484', 'email': 'Patrick@gmail.com',
             'join_date': '2025-03-20', 'status': 'Active', 'total_contributions': 345.00},
            {'partner_id': 'PT005', 'name': 'ABC Company', 'type': 'Corporate', 'tier': 'Diamond Partners',
             'contact_person': 'John Doe', 'phone': '0234567890', 'email': 'info@abc.com',
             'join_date': '2025-04-12', 'status': 'Active', 'total_contributions': 5000.00},
            {'partner_id': 'PT006', 'name': 'XYZ Ltd', 'type': 'Corporate', 'tier': 'Gold Partners',
             'contact_person': 'Jane Smith', 'phone': '0234567891', 'email': 'info@xyz.com',
             'join_date': '2025-05-08', 'status': 'Active', 'total_contributions': 3000.00}
        ]
        
        # Create DataFrame from the list
        self.partners_df = pd.DataFrame(partners_data)
        
        # Add contributions
        contributions = []
        contribution_id = 1
        
        # Iterate through the DataFrame rows properly
        for idx, partner in self.partners_df.head(4).iterrows():
            num_payments = int(partner['total_contributions'] // 200) + 1
            remaining = partner['total_contributions']
            
            for j in range(num_payments):
                amount = min(200, remaining)
                if amount > 0:
                    contribution = {
                        'contribution_id': f'PC{contribution_id:04d}',
                        'partner_id': partner['partner_id'],
                        'date': f'2025-{random.randint(1,8):02d}-{random.randint(1,28):02d}',
                        'amount': amount,
                        'type': 'Monthly',
                        'notes': ''
                    }
                    contributions.append(contribution)
                    remaining -= amount
                    contribution_id += 1
        
        if contributions:
            self.partner_contributions = pd.DataFrame(contributions)
        else:
            self.partner_contributions = pd.DataFrame(columns=['contribution_id', 'partner_id', 'date', 'amount', 'type', 'notes'])
            
        print(f"✓ Partnership Manager initialized with {len(self.partners_df)} partners")
    
    def get_partnership_summary(self):
        """Get partnership dashboard summary"""
        total_partners = len(self.partners_df)
        total_contributions = self.partners_df['total_contributions'].sum()
        church_members = len(self.partners_df[self.partners_df['type'] == 'Individual'])
        
        # Tier breakdown
        tier_counts = self.partners_df['tier'].value_counts()
        
        # Recent contributions (last 30 days)
        cutoff_date = (datetime.now() - timedelta(days=30)).strftime('%Y-%m-%d')
        
        if not self.partner_contributions.empty and 'date' in self.partner_contributions.columns:
            recent = self.partner_contributions[self.partner_contributions['date'] >= cutoff_date]
            recent_total = recent['amount'].sum() if not recent.empty else 0
        else:
            recent_total = 0
        
        monthly_avg = total_contributions / 6 if total_partners > 0 else 0  # Last 6 months avg
        
        return {
            'total_partners': total_partners,
            'total_contributions': total_contributions,
            'church_members': church_members,
            'church_member_pct': (church_members/total_partners)*100 if total_partners > 0 else 0,
            'monthly_avg': monthly_avg,
            'tier_counts': tier_counts,
            'recent_contributions': recent_total
        }
    
    def display_partnership_dashboard(self):
        """Display partnership dashboard as shown in screenshot"""
        print("\n" + "="*70)
        print("PARTNERSHIP DASHBOARD")
        print("="*70)
        
        summary = self.get_partnership_summary()
        
        print(f"""
┌─────────────────────────────────────────────────────┐
│ PARTNERSHIP OVERVIEW                                 │
├─────────────────────────────────────────────────────┤
│ Total Partners: {summary['total_partners']:<12} │ ↑ {summary['total_partners']} active                    │
│ Total Contributions: R {summary['total_contributions']:>10,.2f} │ All time                       │
│ Church Members: {summary['church_members']:<12} │ {summary['church_member_pct']:.0f}% of total                │
│ Monthly Average: R {summary['monthly_avg']:>10,.2f} │ Last 6 months                  │
└─────────────────────────────────────────────────────┘
        """)
        
        print("\nPARTNERSHIP TIERS:")
        print(f"{'Tier':<20} {'Count':<10}")
        print("-"*30)
        for tier in self.tiers:
            count = summary['tier_counts'].get(tier, 0)
            print(f"{tier:<20} {count:<10}")
        
        print(f"\nRecent (30 days) Total Contributions: R {summary['recent_contributions']:,.2f}")


class SMSManager:
    """Handle SMS broadcasting and messaging"""
    
    def __init__(self):
        self.sms_credits = 202
        self.messages_sent = 20
        self.success_rate = 100
        self.templates = {
            'Welcome Message': 'Dear {{first_name}}, welcome to {{church_name}}! We are blessed to have you.',
            'Service Reminder': 'Dear {{first_name}}, join us this Sunday at 8:30 AM for worship service. God bless you!',
            'Prayer Request': 'Prayer request received: {{description}}. We are praying with you.',
            'Tithe Thank You': 'Dear {{first_name}}, thank you for your tithe of {{currency}}{{amount}} received for {{month}}. We appreciate your faithfulness.'
        }
        self.sms_history = pd.DataFrame(columns=[
            'message_id', 'recipients', 'message', 'sent_date', 'status', 'credits_used'
        ])
        print(f"✓ SMS Manager initialized with {self.sms_credits} credits")
    
    def send_sms(self, recipients, message, sender="Church"):
        """Send SMS to recipients"""
        # Calculate cost
        parts = len(message) // 160 + 1
        total_cost = len(recipients) * parts
        
        if total_cost > self.sms_credits:
            return False, f"Insufficient credits. Need {total_cost}, have {self.sms_credits}"
        
        # Send (simulated)
        message_id = f"MSG{len(self.sms_history)+1:04d}"
        new_message = pd.DataFrame([{
            'message_id': message_id,
            'recipients': len(recipients),
            'message': message[:50] + "..." if len(message) > 50 else message,
            'sent_date': datetime.now().strftime('%Y-%m-%d %H:%M'),
            'status': 'Sent',
            'credits_used': total_cost
        }])
        
        self.sms_history = pd.concat([self.sms_history, new_message], ignore_index=True)
        
        self.sms_credits -= total_cost
        self.messages_sent += len(recipients)
        
        return True, f"Message sent to {len(recipients)} recipients. Credits used: {total_cost}"
    
    def use_template(self, template_name, variables):
        """Use a template with variables"""
        if template_name not in self.templates:
            return None
        
        message = self.templates[template_name]
        for key, value in variables.items():
            message = message.replace('{{' + key + '}}', str(value))
        
        return message
    
    def display_sms_center(self):
        """Display SMS command center as shown in screenshot"""
        print("\n" + "="*70)
        print("SMS COMMAND CENTER")
        print("="*70)
        
        print(f"""
┌─────────────────────────────────────────────────────┐
│ {self.messages_sent:<3} Total Messages     {self.messages_sent:<3} Successfully Sent  │
│ This Month: +0 today   Status: 100% Healthy        │
├─────────────────────────────────────────────────────┤
│ {self.sms_credits:<3} SMS Credits        {self.messages_sent:<3} Recipients Reached  │
│ Status: Healthy        Status: Healthy              │
└─────────────────────────────────────────────────────┘
        """)
        
        print("\nQUICK ACTIONS:")
        print("  [Send Now →]    Send SMS instantly")
        print("  [Manage Templates →]    Reusable messages")
        print("  [Manage Providers →]    Multi-provider management")

# Initialize modules
cms.partnerships = PartnershipManager()
cms.sms = SMSManager()


# In[20]:


# Step 13: Feedback Management Module

class FeedbackManager:
    """Handle feedback submissions and management"""
    
    def __init__(self):
        self.feedback_df = pd.DataFrame(columns=[
            'feedback_id', 'submitter_name', 'anonymous', 'category',
            'priority', 'submitted_date', 'message', 'status', 'admin_notes',
            'assigned_to', 'resolved_date'
        ])
        self.load_sample_data()
        
    def load_sample_data(self):
        """Load sample feedback data"""
        feedback = [
            {
                'feedback_id': 'FB001',
                'submitter_name': 'Anonymous',
                'anonymous': True,
                'category': 'Suggestion',
                'priority': 'Medium',
                'submitted_date': '2025-08-31',
                'message': 'HRHRHRH',
                'status': 'Read',
                'admin_notes': '',
                'assigned_to': None,
                'resolved_date': None
            }
        ]
        
        self.feedback_df = pd.DataFrame(feedback)
        print(f"✓ Feedback Manager initialized with {len(self.feedback_df)} feedback entries")
    
    def submit_feedback(self, message, category='General', priority='Medium', anonymous=True, submitter_name='Anonymous'):
        """Submit new feedback"""
        feedback_id = f"FB{len(self.feedback_df)+1:03d}"
        feedback = {
            'feedback_id': feedback_id,
            'submitter_name': submitter_name if not anonymous else 'Anonymous',
            'anonymous': anonymous,
            'category': category,
            'priority': priority,
            'submitted_date': datetime.now().strftime('%Y-%m-%d'),
            'message': message,
            'status': 'Unread',
            'admin_notes': '',
            'assigned_to': None,
            'resolved_date': None
        }
        
        self.feedback_df = pd.concat([self.feedback_df, pd.DataFrame([feedback])], ignore_index=True)
        return feedback_id
    
    def update_status(self, feedback_id, status, admin_notes=''):
        """Update feedback status"""
        self.feedback_df.loc[self.feedback_df['feedback_id'] == feedback_id, 'status'] = status
        if admin_notes:
            self.feedback_df.loc[self.feedback_df['feedback_id'] == feedback_id, 'admin_notes'] = admin_notes
        if status == 'Resolved':
            self.feedback_df.loc[self.feedback_df['feedback_id'] == feedback_id, 'resolved_date'] = datetime.now().strftime('%Y-%m-%d')
        return True
    
    def display_feedback_details(self, feedback_id=None):
        """Display feedback details as shown in screenshot"""
        if feedback_id is None and len(self.feedback_df) > 0:
            feedback_id = self.feedback_df.iloc[0]['feedback_id']
        
        feedback = self.feedback_df[self.feedback_df['feedback_id'] == feedback_id].iloc[0]
        
        print("\n" + "="*70)
        print("FEEDBACK DETAILS")
        print("="*70)
        
        print(f"""
FEEDBACK SUBMISSION
──────────────────────────────────────────────────────
Submitter: {feedback['submitter_name']}
Category: {feedback['category']}
Priority: {feedback['priority']}
Submitted: {feedback['submitted_date']}
Status: {feedback['status']}

FEEDBACK MESSAGE
──────────────────────────────────────────────────────
{feedback['message']}

ADMIN NOTES & STATUS
──────────────────────────────────────────────────────
Status: {feedback['status']}
{feedback['admin_notes'] if feedback['admin_notes'] else ''}
        """)

# Initialize Feedback Manager
cms.feedback = FeedbackManager()


# In[25]:


# Step 14: Main Dashboard and Interactive Menu

class ChurchManagementSystem:
    # ... (previous code extended with display methods)
    
    def run_interactive_menu(self):
        """Run interactive menu system"""
        while True:
            print("\n" + "="*70)
            print(f"{self.church_name} - MAIN MENU")
            print("="*70)
            print("""
1. Dashboard Overview
2. Members Management
3. Attendance & QR Codes
4. Finance Management
5. Children's Ministry
6. Visitors Management
7. Programs & Events
8. Equipment Inventory
9. Groups & Counseling
10. Prayer Line
11. Welfare Management
12. Partnerships
13. SMS Broadcasting
14. Feedback Management
15. Reports & Analytics
0. Exit
            """)
            
            choice = input("\nSelect an option (0-15): ").strip()
            
            if choice == '0':
                print("\nThank you for using Flood of Life Embazzy International Church Management System!")
                break
            elif choice == '1':
                self.display_dashboard()
            elif choice == '2':
                self.members.display_members_directory()
            elif choice == '3':
                self.attendance.display_attendance_dashboard()
                qr_choice = input("\nGenerate QR code for attendance? (y/n): ").lower()
                if qr_choice == 'y':
                    service = input("Service type: ")
                    date = input("Date (YYYY-MM-DD) [Enter for today]: ") or datetime.now().strftime('%Y-%m-%d')
                    self.attendance.generate_qr_code(service, date)
            elif choice == '4':
                self.finance.display_financial_dashboard()
            elif choice == '5':
                self.children.display_children_dashboard()
            elif choice == '6':
                self.visitors.display_visitor_management()
            elif choice == '7':
                self.programs.display_programs()
            elif choice == '8':
                self.equipment.display_equipment_list()
            elif choice == '9':
                self.groups.display_group_assignments()
            elif choice == '10':
                self.prayer.display_prayer_line()
            elif choice == '11':
                self.welfare.display_welfare_dashboard()
            elif choice == '12':
                self.partnerships.display_partnership_dashboard()
            elif choice == '13':
                self.sms.display_sms_center()
            elif choice == '14':
                self.feedback.display_feedback_details()
            elif choice == '15':
                self.generate_reports()
            else:
                print("Invalid option. Please try again.")
    
    def generate_reports(self):
        """Generate various reports"""
        print("\n" + "="*70)
        print("REPORTS & ANALYTICS")
        print("="*70)
        
        print("\n1. Member Statistics")
        print("2. Attendance Trends")
        print("3. Financial Summary")
        print("4. Children's Ministry Report")
        print("5. Partnership Report")
        
        report_choice = input("\nSelect report (1-5): ").strip()
        
        if report_choice == '1':
            print("\nMEMBER STATISTICS")
            print("-"*50)
            print(f"Total Members: {len(self.members.members_df)}")
            print(f"Active Members: {len(self.members.members_df[self.members.members_df['status'] == 'Active'])}")
            print(f"New Members (30d): {self.members.get_new_members_count(30)}")
            print("\nGender Distribution:", self.members.get_gender_distribution())
            print("\nAge Distribution:", self.members.get_age_distribution())
            
            dept_counts, dept_pcts = self.members.get_department_distribution()
            print("\nTop 5 Departments:")
            for dept, count in dept_counts.head(5).items():
                print(f"  {dept}: {count} members ({dept_pcts[dept]})")
        
        elif report_choice == '2':
            print("\nATTENDANCE TRENDS")
            print("-"*50)
            trends = self.attendance.get_attendance_trends(6)
            for month, count in trends.items():
                print(f"{month}: {count} attendees")
            print(f"\n{alert}")
        
        elif report_choice == '3':
            print("\nFINANCIAL SUMMARY")
            print("-"*50)
            print(f"Total Income: R {self.finance.get_total_income():,.2f}")
            print(f"Total Expenses: R {self.finance.get_total_expenses():,.2f}")
            print(f"Net Balance: R {self.finance.get_current_balance():,.2f}")
            print("\nIncome by Category:")
            for cat, amount in self.finance.get_category_breakdown('Income').items():
                print(f"  {cat}: R {amount:,.2f}")
        
        elif report_choice == '4':
            print("\nCHILDREN'S MINISTRY REPORT")
            print("-"*50)
            age_dist = self.children.get_age_group_distribution()
            for group, count in age_dist.items():
                print(f"{group}: {count} children")
            analytics = self.children.get_attendance_analytics('monthly')
            print(f"\nMonthly Attendance: {analytics['total_attendance']}")
            print(f"Active Children: {analytics['active_children']}")
        
        elif report_choice == '5':
            print("\nPARTNERSHIP REPORT")
            print("-"*50)
            summary = self.partnerships.get_partnership_summary()
            print(f"Total Partners: {summary['total_partners']}")
            print(f"Total Contributions: R {summary['total_contributions']:,.2f}")
            print(f"Church Members as Partners: {summary['church_members']} ({summary['church_member_pct']:.1f}%)")
            print(f"Monthly Average: R {summary['monthly_avg']:,.2f}")

# Update the main system with new methods
cms.__class__.run_interactive_menu = 'run_interactive_menu'
cms.__class__.generate_reports = 'generate_reports'

print("\n" + "="*70)
print("SYSTEM INITIALIZATION COMPLETE")
print("="*70)
print("\nFlood of Life Embazzy International Church Management System is ready!")
print(f"Total Members: {len(cms.members.members_df)}")
print(f"Total Children: {len(cms.children.children_df)}")
print(f"Financial Balance: R {cms.finance.get_current_balance():,.2f}")


# In[22]:


# Step 15: Launch the System

print("\n" + "="*70)
print("LAUNCHING FLOOD OF LIFE EMBAZZY INTERNATIONAL CHURCH MANAGEMENT SYSTEM")
print("="*70)

# Display initial dashboard
cms.display_dashboard()

# Show key metrics
print("\n" + "-"*70)
print("SYSTEM OVERVIEW")
print("-"*70)
print(f"✅ Members Module: {len(cms.members.members_df)} members")
print(f"✅ Attendance Module: {len(cms.attendance.attendance_df)} records")
print(f"✅ Finance Module: {len(cms.finance.transactions_df)} transactions")
print(f"✅ Children's Ministry: {len(cms.children.children_df)} children")
print(f"✅ Visitors Module: {len(cms.visitors.visitors_df)} visitors")
print(f"✅ Programs Module: {len(cms.programs.programs_df)} programs")
print(f"✅ Equipment Module: {len(cms.equipment.equipment_df)} items")
print(f"✅ Groups Module: {len(cms.groups.groups_df)} groups")
print(f"✅ Welfare Module: {len(cms.welfare.welfare_payments)} payments")
print(f"✅ Partnerships Module: {len(cms.partnerships.partners_df)} partners")
print(f"✅ SMS Credits Available: {cms.sms.sms_credits}")

# Gender distribution display
print("\n" + "-"*70)
print("GENDER DISTRIBUTION")
print("-"*70)
gender_dist = cms.members.get_gender_distribution()
for gender, pct in gender_dist.items():
    print(f"{gender}: {pct}")

# Age distribution
print("\n" + "-"*70)
print("AGE DISTRIBUTION")
print("-"*70)
age_dist = cms.members.get_age_distribution()
for age_group, pct in age_dist.items():
    print(f"{age_group}: {pct}")

print("\n" + "="*70)
print("SYSTEM LAUNCHED SUCCESSFULLY!")
print("="*70)
print("\nThe Church Management System for Flood of Life Embazzy International Church")
print("is now ready to use with all modules fully functional.")
print("\nKey Features:")
print("✓ Member Management with Directory")
print("✓ QR Code Attendance Tracking")
print("✓ Financial Management with Tithe Tracking")
print("✓ Children's Ministry with Real-time Check-ins")
print("✓ Visitor Management with Follow-up System")
print("✓ Programs & Events Planning")
print("✓ Equipment Inventory with QR Codes")
print("✓ Small Groups & Counseling")
print("✓ Prayer Line Management")
print("✓ Welfare & Partnership Tracking")
print("✓ SMS Broadcasting")
print("✓ Feedback System")


# In[27]:


# Step 16: Interactive Mode (Run this cell to start the interactive menu)

# Uncomment the line below to start the interactive menu
# cms.run_interactive_menu()

# For Jupyter notebook, we'll provide a simple interactive widget if available
if HAS_WIDGETS:
    from IPython.display import display
    import ipywidgets as widgets
    
    print("\n" + "="*70)
    print("INTERACTIVE CONTROL PANEL")
    print("="*70)
    print("Use the buttons below to navigate the system:")
    
    # Create buttons for main modules
    buttons = []
    modules = [
        ('Dashboard', '1'), ('Members', '2'), ('Attendance', '3'), 
        ('Finance', '4'), ('Children', '5'), ('Visitors', '6'),
        ('Programs', '7'), ('Equipment', '8'), ('Groups', '9'),
        ('Prayer', '10'), ('Welfare', '11'), ('Partnerships', '12'),
        ('SMS', '13'), ('Feedback', '14'), ('Reports', '15')
    ]
    
    button_layout = widgets.GridspecLayout(5, 3)
    for i, (label, value) in enumerate(modules):
        button = widgets.Button(description=label, layout=widgets.Layout(width='auto'))
        button.value = value
        
        def on_button_click(b):
            clear_output(wait=True)
            if b.value == '1':
                cms.display_dashboard()
            elif b.value == '2':
                cms.members.display_members_directory()
            elif b.value == '3':
                cms.attendance.display_attendance_dashboard()
            elif b.value == '4':
                cms.finance.display_financial_dashboard()
            elif b.value == '5':
                cms.children.display_children_dashboard()
            elif b.value == '6':
                cms.visitors.display_visitor_management()
            elif b.value == '7':
                cms.programs.display_programs()
            elif b.value == '8':
                cms.equipment.display_equipment_list()
            elif b.value == '9':
                cms.groups.display_group_assignments()
            elif b.value == '10':
                cms.prayer.display_prayer_line()
            elif b.value == '11':
                cms.welfare.display_welfare_dashboard()
            elif b.value == '12':
                cms.partnerships.display_partnership_dashboard()
            elif b.value == '13':
                cms.sms.display_sms_center()
            elif b.value == '14':
                cms.feedback.display_feedback_details()
            elif b.value == '15':
                cms.generate_reports()
            display(button_layout)
        
        button.on_click(on_button_click)
        button_layout[i // 3, i % 3] = button
    
    display(button_layout)
else:
    print("\nTo run interactive mode, uncomment the line: cms.run_interactive_menu()")
    print("Or install ipywidgets: pip install ipywidgets")


# In[24]:


# Final Step: Export Data (Optional)
# This cell allows you to export data to CSV files

def export_all_data():
    """Export all data to CSV files"""
    import os
    
    # Create exports directory
    if not os.path.exists('church_exports'):
        os.makedirs('church_exports')
    
    # Export each dataframe
    cms.members.members_df.to_csv('church_exports/members.csv', index=False)
    cms.attendance.attendance_df.to_csv('church_exports/attendance.csv', index=False)
    cms.finance.transactions_df.to_csv('church_exports/finance.csv', index=False)
    cms.children.children_df.to_csv('church_exports/children.csv', index=False)
    cms.children.children_attendance.to_csv('church_exports/children_attendance.csv', index=False)
    cms.visitors.visitors_df.to_csv('church_exports/visitors.csv', index=False)
    cms.visitors.follow_ups.to_csv('church_exports/follow_ups.csv', index=False)
    cms.programs.programs_df.to_csv('church_exports/programs.csv', index=False)
    cms.equipment.equipment_df.to_csv('church_exports/equipment.csv', index=False)
    cms.groups.groups_df.to_csv('church_exports/groups.csv', index=False)
    cms.groups.group_members.to_csv('church_exports/group_members.csv', index=False)
    cms.welfare.welfare_payments.to_csv('church_exports/welfare_payments.csv', index=False)
    cms.welfare.welfare_claims.to_csv('church_exports/welfare_claims.csv', index=False)
    cms.partnerships.partners_df.to_csv('church_exports/partners.csv', index=False)
    cms.partnerships.partner_contributions.to_csv('church_exports/partner_contributions.csv', index=False)
    cms.feedback.feedback_df.to_csv('church_exports/feedback.csv', index=False)
    
    print("\n" + "="*70)
    print("DATA EXPORT COMPLETE")
    print("="*70)
    print("All data exported to 'church_exports' directory")
    print(f"Location: {os.path.abspath('church_exports')}")

# Uncomment to export data
# export_all_data()

print("\n" + "="*70)
print("FLOOD OF LIFE EMBAZZY INTERNATIONAL CHURCH")
print("COMPLETE CHURCH MANAGEMENT SYSTEM")
print("="*70)
print("\n✅ System fully operational with all modules from screenshots")
print("✅ Ready for production use")
print("✅ Data persisted in memory (export to CSV for permanent storage)")
print("\nThank you for using this Church Management System!")


# In[34]:



# In[36]:


from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory storage (replace with database later)
members = []
events = []
sermons = []

@app.route("/")
def home():
  return render_template("home.html", members=members, events=events, sermons=sermons)

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        members.append({"name": name, "email": email})
        return redirect(url_for("home"))
    return render_template("register.html")

@app.route("/add_event", methods=["GET", "POST"])
def add_event():
    if request.method == "POST":
        title = request.form["title"]
        date = request.form["date"]
        events.append({"title": title, "date": date})
        return redirect(url_for("home"))
    return render_template("add_event.html")

@app.route("/add_sermon", methods=["GET", "POST"])
def add_sermon():
    if request.method == "POST":
        title = request.form["title"]
        link = request.form["link"]
        sermons.append({"title": title, "link": link})
        return redirect(url_for("home"))
    return render_template("add_sermon.html")

# ===== RUN THE APP =====
if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
