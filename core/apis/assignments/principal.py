from flask import Blueprint
from core.apis import decorators
from core.models.assignments import Assignment
from .schema import AssignmentSchema
from core.apis.responses import APIResponse

principal_assignments_resources = Blueprint('principal_assignments_resources', __name__)

@principal_assignments_resources.route('/assignments',methods=['GET'], strict_slashes=False)
@decorators.authenticate_principal
def list_assignments(p):
    """List all submitted and graded assignments"""
    students_assignments = Assignment.get_assignments_submitted_graded()
    students_assignments_dump = AssignmentSchema().dump(students_assignments, many=True)
    return APIResponse.respond(data=students_assignments_dump)