
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'DIV LPAR MINUS MUL NUMBER PLUS POW RPARexpression : expression PLUS termexpression : expression MINUS termexpression : termterm : term MUL powerterm : term DIV powerterm : powerpower : factor POW powerpower : factorfactor : NUMBERfactor : LPAR expression RPAR'
    
_lr_action_items = {'NUMBER':([0,6,7,8,9,10,11,],[5,5,5,5,5,5,5,]),'LPAR':([0,6,7,8,9,10,11,],[6,6,6,6,6,6,6,]),'$end':([1,2,3,4,5,13,14,15,16,17,18,],[0,-3,-6,-8,-9,-1,-2,-4,-5,-7,-10,]),'PLUS':([1,2,3,4,5,12,13,14,15,16,17,18,],[7,-3,-6,-8,-9,7,-1,-2,-4,-5,-7,-10,]),'MINUS':([1,2,3,4,5,12,13,14,15,16,17,18,],[8,-3,-6,-8,-9,8,-1,-2,-4,-5,-7,-10,]),'RPAR':([2,3,4,5,12,13,14,15,16,17,18,],[-3,-6,-8,-9,18,-1,-2,-4,-5,-7,-10,]),'MUL':([2,3,4,5,13,14,15,16,17,18,],[9,-6,-8,-9,9,9,-4,-5,-7,-10,]),'DIV':([2,3,4,5,13,14,15,16,17,18,],[10,-6,-8,-9,10,10,-4,-5,-7,-10,]),'POW':([4,5,18,],[11,-9,-10,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expression':([0,6,],[1,12,]),'term':([0,6,7,8,],[2,2,13,14,]),'power':([0,6,7,8,9,10,11,],[3,3,3,3,15,16,17,]),'factor':([0,6,7,8,9,10,11,],[4,4,4,4,4,4,4,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> expression","S'",1,None,None,None),
  ('expression -> expression PLUS term','expression',3,'p_expression_add','expressions_parser.py',6),
  ('expression -> expression MINUS term','expression',3,'p_expression_sub','expressions_parser.py',10),
  ('expression -> term','expression',1,'p_expression_term','expressions_parser.py',14),
  ('term -> term MUL power','term',3,'p_term_mul','expressions_parser.py',18),
  ('term -> term DIV power','term',3,'p_term_div','expressions_parser.py',22),
  ('term -> power','term',1,'p_term_power','expressions_parser.py',26),
  ('power -> factor POW power','power',3,'p_power_raise','expressions_parser.py',30),
  ('power -> factor','power',1,'p_power_factor','expressions_parser.py',34),
  ('factor -> NUMBER','factor',1,'p_factor_num','expressions_parser.py',38),
  ('factor -> LPAR expression RPAR','factor',3,'p_factor_expr','expressions_parser.py',42),
]
