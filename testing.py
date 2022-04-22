from flask import Blueprint, jsonify, request
from data import db_session, jobs


blueprint = Blueprint("jobs_api", __name__, template_folder="templates")


@blueprint.route("/api/jobs/<int:jobs_id>", methods=["DELETE"])
def delete_job(jobs_id):
    session = db_session.create_session()
    jobs_box = session.query(jobs.Jobs).get(jobs_id)

    if not jobs_box:
        return jsonify({"error": "Ошибка! Не найдено."})

    session.delete(jobs_box)
    session.commit()

    return jsonify({"success": "ОК"})