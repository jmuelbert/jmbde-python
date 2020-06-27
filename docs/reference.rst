{%- macro heading(text) -%}
{{text}}
{% for _ in text %}-{% endfor %}
{%- endmacro -%}
Reference
=========

.. contents::
    :local:
    :backlinks: none


{{ heading(jmbde + ".__main__") }}

.. automodule:: jmbde.__main__
   :members:
