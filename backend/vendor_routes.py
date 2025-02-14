from flask import Blueprint, jsonify, request

vendor_bp = Blueprint('vendor_bp', __name__)

# Sample vendor data (temporary storage, replace with database later)
vendors = [
    {"id": 1, "name": "Vendor A", "status": "Pending"},
    {"id": 2, "name": "Vendor B", "status": "Approved"}
]

# Get all vendors
@vendor_bp.route('/vendors', methods=['GET'])
def get_vendors():
    return jsonify(vendors)

# Get a single vendor by ID
@vendor_bp.route('/vendors/<int:vendor_id>', methods=['GET'])
def get_vendor(vendor_id):
    vendor = next((v for v in vendors if v["id"] == vendor_id), None)
    if vendor:
        return jsonify(vendor)
    return jsonify({"error": "Vendor not found"}), 404

# Add a new vendor
@vendor_bp.route('/vendors', methods=['POST'])
def add_vendor():
    new_vendor = request.json
    new_vendor["id"] = len(vendors) + 1
    vendors.append(new_vendor)
    return jsonify({"message": "Vendor added successfully", "vendor": new_vendor}), 201

# Update vendor details
@vendor_bp.route('/vendors/<int:vendor_id>', methods=['PUT'])
def update_vendor(vendor_id):
    vendor = next((v for v in vendors if v["id"] == vendor_id), None)
    if vendor:
        data = request.json
        vendor.update(data)
        return jsonify({"message": "Vendor updated successfully", "vendor": vendor})
    return jsonify({"error": "Vendor not found"}), 404

# Delete a vendor
@vendor_bp.route('/vendors/<int:vendor_id>', methods=['DELETE'])
def delete_vendor(vendor_id):
    global vendors
    vendors = [v for v in vendors if v["id"] != vendor_id]
    return jsonify({"message": "Vendor deleted successfully"})
