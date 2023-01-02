from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from stoffer.api.schemas import SMAuthSchema
from stoffer.models import SMAuth
from stoffer.extensions import db
from stoffer.commons.pagination import paginate
from flask_jwt_extended import get_jwt_identity
from marshmallow import INCLUDE


class SMAuthResource(Resource):
    """Single object resource

    ---
    get:
      tags:
        - api
      responses:
        200:
          content:
            application/json:
              schema:
                allOf:
                  - $ref: '#/components/schemas/PaginatedResult'
                  - type: object
                    properties:
                      results:
                        type: array
                        items:
                          $ref: '#/components/schemas/SMAuthSchema'
    post:
      tags:
        - api
      requestBody:
        content:
          application/json:
            schema:
              SMAuthSchema
      responses:
        201:
          content:
            application/json:
              schema:
                type: object
                properties:
                  msg:
                    type: string
                    example: exec created
                  exec: SMAuthSchema
    put:
      tags:
        - api
      requestBody:
        content:
          application/json:
            schema:
              SMAuthSchema
      responses:
        200:
          content:
            application/json:
              schema:
                type: object
                properties:
                  msg:
                    type: string
                    example: exec updated
                  exec: SMAuthSchema
        404:
          description: smauth does not exists
    delete:
      tags:
        - api
      requestBody:
        content:
          application/json:
            schema:
              SMAuthSchema
      responses:
        200:
          content:
            application/json:
              schema:
                type: object
                properties:
                  msg:
                    type: string
                    example: smauth deleted
        404:
          description: smauth does not exists
    """
    method_decorators = [jwt_required()]

    def get(self):
        user_id = get_jwt_identity()
        schema = SMAuthSchema(many=True)
        query = SMAuth.query.filter_by(user_id=user_id)
        
        return paginate(query, schema)

    def post(self):
        if not request.is_json:
            return {"msg": "Missing JSON in request"}, 400
        
        schema = SMAuthSchema(partial=True, unknown=INCLUDE)
        uid = get_jwt_identity()

        request.json['user_id'] = uid
        
        sa = schema.load(request.json)
        db.session.add(sa)
        db.session.commit()

        print(sa.user_id, sa)
        return {"msg": "smauth updated", "smauth": schema.dump(sa)}

    def put(self):
        if not request.is_json:
            return {"msg": "Missing JSON in request"}, 400
        eid = request.json.get('id', -1)
        if eid < 0:
            return {"msg": "Missing pid"}, 400
        uid = get_jwt_identity()
        schema = SMAuthSchema(partial=True, unknown=INCLUDE)
        smauth = SMAuth.query.filter_by(id=eid, user_id=uid).first()
        if smauth is None:
            return {"msg": "No such smauth"}, 400
        smauth = schema.load(request.json, instance=smauth)
        db.session.commit()
        return {"msg": "smauth updated", "smauth": schema.dump(smauth)}

    def delete(self):
        if not request.is_json:
            return {"msg": "Missing JSON in request"}, 400
        eid = request.json.get('id', -1)
        if eid < 0:
            return {"msg": "Missing eid"}, 400
        uid = get_jwt_identity()
        schema = SMAuthSchema(partial=True, unknown=INCLUDE)
        smauth = SMAuth.query.filter_by(id=eid, user_id=uid).first()
        if smauth is None:
            return {"msg": "No such smauth"}, 400
        name = smauth.id
        db.session.delete(smauth)
        db.session.commit()

        return {"msg": f"smauth '{ name }' deleted"}