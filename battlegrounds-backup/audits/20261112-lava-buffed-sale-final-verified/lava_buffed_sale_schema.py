"""Strict frozen V2 real-result schema. No execution, no fabricated runtime evidence."""
import re
SCOPE='one ordinary Lava first Mini permanent buff then native sale with live Mini regrant'
FULL_MARKERS={'real_temporary_spell_and_reset_lava_before_cast': 1, 'other_original_board_target_held_no_consumption': 1, 'public_native_first_trident_cast': 1, 'first_trident_permanent_exact_plus2_kept1_no_temporary_layer': 1, 'cast_consumes_original_token_only_no_factory_rng_stock': 1, 'mini_cast_does_not_consume_darkcrest_growth_or_source_state': 1, 'actual_completed_cast_updates_only_observer_receipt': 1, 'used_original_token_replay_rejected_without_mutation': 1, 'original_live_mini_required_before_buffed_sale': 1, 'original_buffed_lava_sale_preflight': 1, 'copied_wrongowner_buffed_lava_sale_refused': 1, 'unbound_buffed_lava_sale_preserves_state': 1, 'public_native_buffed_lava_sell': 1, 'buffed_sale_only_original_board_departure': 1, 'buffed_sale_exact_native_accounting': 1, 'buffed_sale_no_uid_rng_and_original_absent': 1, 'buffed_lava_authority_retired': 1, 'live_mini_not_retired_by_lava_sale': 1, 'mini_token_record_reference_survives_lava_sale': 1, 'buffed_stats_do_not_leak_to_native_factory_preview': 1, 'actual_buffed_retirement_history_owner_bound': 1, 'actual_retirement_history_blocks_buy_and_play_gate': 1, 'history_gate_checks_do_not_change_live_state': 1, 'retired_buffed_lava_replay_refused_no_mutation': 1, 'original_mini_publicplay_real_waiting_grant': 1, 'one_nonempty_post_lava_sale_combat': 1, 'actual_combat_mini_present_lava_absent': 1, 'buffed_history_buy_gate_persists_next_round': 1, 'live_mini_native_regrant_without_lava': 1, 'no_lava_new_token_cast_held_without_consumption': 1, 'matrix_result_file': 1, 'complete_game_script': 1, 'complete_catalog': 1, 'same_game_native_child_preview_created': 1, 'native_preview_does_not_change_live_state_or_receipts': 1, 'native_preview_complete_child_shape_matches': 1, 'native_four_player_full_23_card_room': 1, 'mini_lava_original_hand_before_play': 1, 'copied_mini_token_rejected': 1, 'wrong_owner_mini_token_rejected': 1, 'copied_lava_target_rejected': 1, 'fabricated_mini_cast_context_rejected': 1, 'mini_preconsume_negative_calls_leave_full_state_unchanged': 1, 'actual_original_lava_preflight': 1, 'copied_lava_preflight_rejected': 1, 'wrong_owner_preflight_rejected': 1, 'fabricated_live_play_context_rejected': 1, 'no_live_completion_without_native_context': 1, 'preplay_rejections_preserve_all_live_state': 1, 'original_lava_object_unchanged_after_play': 1, 'actual_completed_original_lava_board_custody': 1, 'copied_board_lava_rejected': 1, 'wrong_owner_board_lava_rejected': 1, 'completed_transaction_replay_rejected': 1, 'postplay_rejections_clear_and_preserve_live_state': 1, 'lava_play_is_only_original_hand_to_board_no_birth_rng_or_stock': 1, 'native_parent_offer_and_gold': 1, 'native_parent_purchase': 1, 'pre_source_original_purchase_BG23_000': 1, 'pre_source_original_purchase_BG23_009': 1, 'public_original_lava_play_position_0': 1, 'native_eot_context_released': 1, 'one_real_mini_trident_in_original_hand': 3, 'original_waiting_token_bound_to_exact_mini_owner_round': 3, 'pre_source_public_tavern_upgrade_3': 1, 'pre_source_public_tavern_upgrade_4': 1, 'pre_source_public_tavern_upgrade_5': 1, 'native_opponent_tier1_offer_and_gold_1': 1, 'native_opponent_tier1_offer_and_gold_2': 1, 'native_opponent_tier1_offer_and_gold_3': 1, 'opponent_public_buy_1': 1, 'opponent_public_buy_2': 1, 'opponent_public_buy_3': 1, 'opponent_public_nonempty_board_1': 1, 'opponent_public_nonempty_board_2': 1, 'opponent_public_nonempty_board_3': 1, 'native_opponent_ready_1': 1, 'native_opponent_ready_2': 1, 'native_opponent_ready_3': 1}

def ordered_markers(round_number):
 return ['public_native_first_trident_cast','original_live_mini_required_before_buffed_sale','original_buffed_lava_sale_preflight','public_native_buffed_lava_sell','buffed_lava_authority_retired','actual_retirement_history_blocks_buy_and_play_gate','native_eot_combat_next_recruit_'+str(round_number),'buffed_history_buy_gate_persists_next_round','live_mini_native_regrant_without_lava','no_lava_new_token_cast_held_without_consumption']

def validate_full(r,log,evidence):
 require=r.require;exact=r.exact_keys;ints=r.integer_fields
 require(r.NEW_VALIDATORS_READY is True,'UNKNOWN exact buffed Lava sale validator')
 lines=log.splitlines();prefix='DARKCREST_LAVA_BUFFED_SALE_REAL_MATRIX_PASS'
 require(lines.count('DARKCREST_LAVA_BUFFED_SALE_MATRIX_LOAD_BEGIN')==1,'Exactly one new initializer')
 markers=[line for line in lines if line.startswith(prefix)];require(len(markers)==1,'Exactly one full result')
 match=re.fullmatch(prefix+r' cases=1 casts=1 combats=1 checks=([1-9][0-9]*)',markers[0]);require(match is not None,'Exact one-case/cast/combat result')
 count=int(match.group(1));require(sum(line.startswith('PASS ') for line in lines)==count,'Dynamic PASS count mismatch')
 r.marker_counts(log,FULL_MARKERS)
 path=evidence/r.NEW_TEST_METADATA['scenario_file'];require(path.is_file() and not path.is_symlink(),'Actual external scenario required')
 row=r.read_json(path)
 exact(row,['scope','seed','checks','sale','casts','darkcrest_uid','darkcrest_final_tier','mini_uid','old_token_uid','new_token_uid','combat_start','native_preview_diagnostic','acquisitions','coin_pre_source_fixture','entirely_natural_game','actual_lava_rebuy_tested','old_full_matrix_repeated'],'buffed Lava sale scenario')
 ints(row,['seed','checks','darkcrest_final_tier'])
 require(row['scope']==SCOPE==r.NEW_TEST_METADATA['scope'] and row['seed']==20261120,'Exact scoped seed')
 require(row['checks']==count-1 and row['darkcrest_final_tier']==2,'Pre-file count and acquisition-card level')
 require(row['coin_pre_source_fixture'] is True,'Disclosed Coin fixture required')
 for key in ['entirely_natural_game','actual_lava_rebuy_tested','old_full_matrix_repeated']:require(row[key] is False,'Unproven claim '+key)
 r.validate_native_preview(row['native_preview_diagnostic'],log)
 sale=row['sale'];exact(sale,['lava_uid','mini_uid','index','retirement','departed_stats','gold_before','gold_after','sold_before','sold_after','stock_before','stock_after','uid_before','uid_after','rng_before','rng_after','native_preview_attack','native_preview_health','preview_not_actual_rebuy','owner_bound_history_gate_observed','actual_shop_buy_attempted'],'native buffed Lava sale')
 ints(sale,['index','gold_before','gold_after','sold_before','sold_after','stock_before','stock_after','uid_before','uid_after','rng_before','rng_after','native_preview_attack','native_preview_health'])
 bodies=[row['mini_uid'],sale['lava_uid'],row['darkcrest_uid']]
 for uid in bodies:r.native_uid(uid)
 require(len(set(bodies))==3 and sale['mini_uid']==row['mini_uid'] and sale['index']==0,'Exact original sale/source/position')
 old_token=r.native_uid(row['old_token_uid']);new_token=r.native_uid(row['new_token_uid'])
 require(old_token>max(r.native_uid(x) for x in bodies) and new_token>old_token,'Distinct original native token identities')
 require(sale['uid_before']==sale['uid_after']>old_token and new_token>=sale['uid_after'],'Sale allocates no UID; later regrant is new')
 for key in ['gold','sold','stock']:require(sale[key+'_before']>=0 and sale[key+'_after']==sale[key+'_before']+1,'Exact native '+key+' delta')
 require(sale['rng_before']==sale['rng_after'],'Sale must not change RNG')
 require((sale['native_preview_attack'],sale['native_preview_health'])==(2,5),'Returned stock/native preview must not inherit buff')
 require(sale['preview_not_actual_rebuy'] is True and sale['owner_bound_history_gate_observed'] is True and sale['actual_shop_buy_attempted'] is False,'Only actual-ledger denial observation, not real shop rebuy')
 retirement=sale['retirement'];exact(retirement,['owner','round','sequence','mini_buffed'],'native retirement');ints(retirement,['owner','round','sequence'])
 require(retirement['owner']==0 and retirement['round']>0 and retirement['sequence']>0 and retirement['mini_buffed'] is True,'Original owner-bound buffed retirement')
 departed=sale['departed_stats'];exact(departed,['attack','health','kept'],'departed stats');ints(departed,['attack','health','kept']);require(departed=={'attack':4,'health':5,'kept':1},'Single first Mini +2 kept1 before sale')
 require(type(row['casts']) is list and len(row['casts'])==1,'Exactly one original cast')
 cast=row['casts'][0];exact(cast,['round','source_uid','token_uid','target_uid','attack_before','attack_after','health','kept'],'first cast');ints(cast,['round','attack_before','attack_after','health','kept'])
 require(cast['round']==retirement['round']>0 and cast['source_uid']==row['mini_uid'] and cast['token_uid']==row['old_token_uid'] and cast['target_uid']==sale['lava_uid'],'Same-round first cast exact source/token/target')
 require((cast['attack_before'],cast['attack_after'],cast['health'],cast['kept'])==(2,4,5,1),'Single native permanent +2, not second buff')
 r.marker_counts(log,{'public_darkcrest_play_'+row['darkcrest_uid']:1,'native_eot_combat_next_recruit_'+str(cast['round']):1,'native_growth_exact_once_'+str(cast['round']):1})
 ordered=ordered_markers(cast['round']);offsets=[lines.index('PASS '+key) for key in ordered];require(offsets==sorted(offsets) and len(set(offsets))==len(offsets),'Actual cast then live Mini precondition then sale then combat then regrant/hold')
 require(type(row['acquisitions']) is list and len(row['acquisitions'])==2,'Two original pre-source acquisitions')
 for acquisition,card,uid,limit in zip(row['acquisitions'],['BG23_000','BG23_009'],bodies[:2],[80,100]):
  exact(acquisition,['id','uid','rolls','source_owned'],'acquisition');ints(acquisition,['rolls']);require(acquisition['id']==card and acquisition['uid']==uid and 0<=acquisition['rolls']<=limit and acquisition['source_owned'] is False,'Original acquisition with bounded rolls')
 combat=row['combat_start'];require(type(combat) is dict,'Actual combat_start event')
 # Native combat event/unit fields are extensible. All scenario-owned dictionaries are exact;
 # here validate mandatory native fields without inventing an exhaustive engine-event schema.
 required={'event','sequence','seed','rules','sort_formation_contract','left','right','left_hand_count','right_hand_count','left_hand_summon_locks','right_hand_summon_locks','round_up_plain_contract'}
 require(required<=set(combat),'Complete native combat_start required');ints(combat,['sequence','seed','left_hand_count','right_hand_count'])
 require(combat['event']=='combat_start' and combat['rules']=='sandbox-1' and combat['sort_formation_contract']=='actual_combat_start_before_start_effects_v1' and combat['sequence']>=0,'Native combat_start identity')
 sides=[];all_uids=[]
 for side in ['left','right']:
  board=combat[side];require(type(board) is list and board,'Nonempty actual combat sides')
  require(type(combat[side+'_hand_summon_locks']) is list and combat[side+'_hand_count']>=0,'Native hand counts and locks')
  for unit in board:
   require(type(unit) is dict,'Native public combat unit');r.native_uid(unit.get('uid'));ints(unit,['attack','health','max_health']);require(unit.get('kind')=='minion' and type(unit.get('golden')) is bool and type(unit.get('card_id')) is str and unit['attack']>=0 and unit['health']>0 and unit['max_health']>=unit['health'],'Native living minion combat shape');all_uids.append(unit['uid'])
  if any(unit['uid']==row['mini_uid'] for unit in board):sides.append(board)
 require(len(set(all_uids))==len(all_uids) and sale['lava_uid'] not in all_uids and len(sides)==1,'Departed Lava absent and exactly one original Mini combat side')
 own=sides[0];require({x['uid'] for x in own}=={row['mini_uid'],row['darkcrest_uid']} and len(own)==2,'Only original Mini and Darkcrest remain on player board')
 for uid,card in [(row['mini_uid'],'BG23_000'),(row['darkcrest_uid'],'BG31_920')]:
  unit=next(x for x in own if x['uid']==uid);require(unit['card_id']==card and unit['golden'] is False,'Original ordinary surviving source bodies')
 return count,row
