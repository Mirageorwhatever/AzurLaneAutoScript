from module.game_setting.setting_extractor import Field

# This file was automatically generated by module/game_setting/setting_extractor.py
# Don't modify it manually.


class GameSettingsGenerated:

    # /controller/command/stage/autobotcommand.lua
    # PlayerPrefs.GetInt("autoBotIsAcitve" .. slot6, 0)
    autoBotIsAcitve = Field(formatter=int, default=0, regex='autoBotIsAcitve(.*)')

    # /gamecfg/activity/entrancedata.lua
    # PlayerPrefs.GetString("permanent_time", "")
    permanent_time = Field(formatter=str, default='', regex='permanent_time')

    # /mgr/crimgr.lua
    # PlayerPrefs.GetFloat("cv_vol", DEFAULT_CVVOLUME)
    cv_vol = Field(formatter=float, default=0.0, regex='cv_vol')
    # PlayerPrefs.GetFloat("bgm_vol", DEFAULT_BGMVOLUME)
    bgm_vol = Field(formatter=float, default=0.0, regex='bgm_vol')
    # PlayerPrefs.GetFloat("se_vol", DEFAULT_SEVOLUME)
    se_vol = Field(formatter=float, default=0.0, regex='se_vol')

    # /mgr/pushnotificationmgr.lua
    # PlayerPrefs.GetInt("push_setting_" .. slot5.id)
    push_setting = Field(formatter=int, default=0, regex='push_setting_(.*)')
    # PlayerPrefs.GetInt("setting_ship_name")
    setting_ship_name = Field(formatter=int, default=0, regex='setting_ship_name')

    # /mgr/uimgr.lua
    # PlayerPrefs.GetInt(SHOW_TOUCH_EFFECT, 1)
    pass  # Unknown

    # /mgr/custom/cpkplaymgr.lua
    # PlayerPrefs.GetFloat("bgm_vol", DEFAULT_BGMVOLUME)
    pass  # Duplicate
    # PlayerPrefs.GetFloat("bgm_vol", DEFAULT_BGMVOLUME)
    pass  # Duplicate

    # /mgr/reddot/reddotmgr.lua
    # PlayerPrefs.GetFloat("firstIntoOtherPanel")
    firstIntoOtherPanel = Field(formatter=float, default=0.0, regex='firstIntoOtherPanel')
    # PlayerPrefs.GetInt("MEMORY_GROUP_NOTIFICATION" .. uv0 .. " " .. slot0, 0)
    MEMORY_GROUP_NOTIFICATION = Field(formatter=int, default=0, regex='MEMORY_GROUP_NOTIFICATION(.*) (.*)')

    # /mgr/tracker/trackermgr.lua
    # PlayerPrefs.GetInt("tracking_" .. slot1, 0)
    tracking = Field(formatter=int, default=0, regex='tracking_(.*)')

    # /mod/battle/battlestate.lua
    # PlayerPrefs.GetInt("autoBotIsAcitve" .. AutoBotCommand.GetAutoBotMark(slot0), 0)
    pass  # Duplicate
    # PlayerPrefs.GetInt("autoSubIsAcitve" .. AutoSubCommand.GetAutoSubMark(slot0), 0)
    autoSubIsAcitve = Field(formatter=int, default=0, regex='autoSubIsAcitve(.*)')
    # PlayerPrefs.GetInt(HIDE_CHAT_FLAG)
    pass  # Unknown

    # /mod/battle/data/battledataproxy.lua
    # PlayerPrefs.GetInt("stage_scratch")
    stage_scratch = Field(formatter=int, default=0, regex='stage_scratch')

    # /mod/battle/view/battleresourcemanager.lua
    # PlayerPrefs.GetInt(BATTLE_HIDE_BG, 1)
    pass  # Unknown

    # /mod/battle/view/ui/battleuimediator.lua
    # PlayerPrefs.GetFloat("joystick_anchorX", slot1.x)
    joystick_anchorX = Field(formatter=float, default=0.0, regex='joystick_anchorX')
    # PlayerPrefs.GetFloat("joystick_anchorY", slot1.y)
    joystick_anchorY = Field(formatter=float, default=0.0, regex='joystick_anchorY')
    # PlayerPrefs.GetFloat("joystick_scale", slot1.scale)
    joystick_scale = Field(formatter=float, default=0.0, regex='joystick_scale')
    # PlayerPrefs.GetFloat("auto_scale", slot1.scale)
    auto_scale = Field(formatter=float, default=0.0, regex='auto_scale')
    # PlayerPrefs.GetFloat("auto_anchorX", slot1.x)
    auto_anchorX = Field(formatter=float, default=0.0, regex='auto_anchorX')
    # PlayerPrefs.GetFloat("auto_anchorY", slot1.y)
    auto_anchorY = Field(formatter=float, default=0.0, regex='auto_anchorY')
    # PlayerPrefs.GetInt(BATTLE_EXPOSE_LINE, 1)
    pass  # Unknown

    # /mod/battle/view/ui/formationpanel/battleskillview.lua
    # PlayerPrefs.GetFloat("skill_" .. slot2 .. "_scale", slot3.scale)
    skill = Field(formatter=float, default=0.0, regex='skill_(.*)_scale')
    # PlayerPrefs.GetFloat("skill_" .. slot2 .. "_anchorX", slot3.x)
    pass  # Duplicate
    # PlayerPrefs.GetFloat("skill_" .. slot2 .. "_anchorY", slot3.y)
    pass  # Duplicate

    # /mod/experiment/world/model/world.lua
    # PlayerPrefs.GetInt(AUTOFIGHT_BATTERY_SAVEMODE, 0)
    pass  # Unknown
    # PlayerPrefs.GetInt(AUTOFIGHT_DOWN_FRAME, 0)
    pass  # Unknown

    # /mod/experiment/world/model/worldconst.lua
    # PlayerPrefs.GetInt("world_help_progress")
    world_help_progress = Field(formatter=int, default=0, regex='world_help_progress')

    # /mod/experiment/world/model/worldstaminamanager.lua
    # PlayerPrefs.GetString("world_stamina_reset_tip", "")
    world_stamina_reset_tip = Field(formatter=str, default='', regex='world_stamina_reset_tip')
    # PlayerPrefs.GetString("world_stamina_reset_tip", "")
    pass  # Duplicate

    # /mod/experiment/world/model/boss/worldbossproxy.lua
    # PlayerPrefs.GetString(slot1 .. getProxy(PlayerProxy):getRawData().id)
    pass  # Unknown

    # /mod/experiment/world/view/svorderpanel.lua
    # PlayerPrefs.GetInt("world_sub_auto_call", 0)
    world_sub_auto_call = Field(formatter=int, default=0, regex='world_sub_auto_call')
    # PlayerPrefs.GetInt("world_sub_call_line", 0)
    world_sub_call_line = Field(formatter=int, default=0, regex='world_sub_call_line')

    # /mod/experiment/world/view/wscommand.lua
    # PlayerPrefs.GetInt("world_skip_precombat", 0)
    world_skip_precombat = Field(formatter=int, default=0, regex='world_skip_precombat')
    # PlayerPrefs.GetInt(slot0[1], 0)
    pass  # Unknown
    # PlayerPrefs.GetInt("auto_switch_mode", 0)
    auto_switch_mode = Field(formatter=int, default=0, regex='auto_switch_mode')
    # PlayerPrefs.GetString("auto_switch_difficult_safe", "only")
    auto_switch_difficult_safe = Field(formatter=str, default='only', regex='auto_switch_difficult_safe')
    # PlayerPrefs.GetString("auto_switch_difficult_base", "all")
    auto_switch_difficult_base = Field(formatter=str, default='all', regex='auto_switch_difficult_base')

    # /mod/experiment/world/view/wsmapright.lua
    # PlayerPrefs.GetInt("world_skip_precombat", 0)
    pass  # Duplicate

    # /model/const/chapterconst.lua
    # PlayerPrefs.GetInt("chapter_skip_battle")
    chapter_skip_battle = Field(formatter=int, default=0, regex='chapter_skip_battle')

    # /model/proxy/activityproxy.lua
    # PlayerPrefs.GetString("Free_Build_Ticket_" .. slot6.id, "")
    Free_Build_Ticket = Field(formatter=str, default='', regex='Free_Build_Ticket_(.*)')

    # /model/proxy/appreciateproxy.lua
    # PlayerPrefs.GetInt("galleryVersion", 0)
    galleryVersion = Field(formatter=int, default=0, regex='galleryVersion')
    # PlayerPrefs.GetInt("musicVersion", 0)
    musicVersion = Field(formatter=int, default=0, regex='musicVersion')
    # PlayerPrefs.GetInt("mangaVersion", 0)
    mangaVersion = Field(formatter=int, default=0, regex='mangaVersion')

    # /model/proxy/chapterproxy.lua
    # PlayerPrefs.GetInt(slot1 .. getProxy(PlayerProxy):getRawData().id)
    pass  # Unknown
    # PlayerPrefs.GetInt("chapter_skip_precombat", 0)
    chapter_skip_precombat = Field(formatter=int, default=0, regex='chapter_skip_precombat')
    # PlayerPrefs.GetInt(AUTOFIGHT_BATTERY_SAVEMODE, 0)
    pass  # Unknown
    # PlayerPrefs.GetInt(AUTOFIGHT_DOWN_FRAME, 0)
    pass  # Unknown

    # /model/proxy/chatproxy.lua
    # PlayerPrefs.GetString(ChatConst.EMOJI_SAVE_TAG .. getProxy(PlayerProxy):getRawData().id)
    pass  # Unknown
    # PlayerPrefs.GetString(ChatConst.EMOJI_ICON_SAVE_TAG .. getProxy(PlayerProxy):getRawData().id)
    pass  # Unknown

    # /model/proxy/coloringproxy.lua
    # PlayerPrefs.GetInt("pixelDraw_maxPage_" .. slot1.id .. "_" .. getProxy(PlayerProxy):getRawData().id, 0)
    pixelDraw_maxPage = Field(formatter=int, default=0, regex='pixelDraw_maxPage_(.*)_(.*)')

    # /model/proxy/dormproxy.lua
    # PlayerPrefs.GetInt("backyard_template" .. getProxy(PlayerProxy):getRawData().id, 0)
    backyard_template = Field(formatter=int, default=0, regex='backyard_template(.*)')
    # PlayerPrefs.GetInt("backyard_template_help" .. getProxy(PlayerProxy):getRawData().id, 0)
    backyard_template_help = Field(formatter=int, default=0, regex='backyard_template_help(.*)')

    # /model/proxy/emojiproxy.lua
    # PlayerPrefs.GetString(uv0.NEW_EMOJI_SAVE_TAG .. getProxy(PlayerProxy):getRawData().id)
    pass  # Unknown

    # /model/proxy/guildproxy.lua
    # PlayerPrefs.GetInt("guild_battle_btn_flag" .. getProxy(PlayerProxy):getRawData().id, 0)
    guild_battle_btn_flag = Field(formatter=int, default=0, regex='guild_battle_btn_flag(.*)')

    # /model/proxy/navalacademyproxy.lua
    # PlayerPrefs.GetString("NavTacticsRecentShipId" .. getProxy(PlayerProxy):getRawData().id)
    NavTacticsRecentShipId = Field(formatter=str, default='', regex='NavTacticsRecentShipId(.*)')

    # /model/proxy/servernoticeproxy.lua
    # PlayerPrefs.GetInt(uv0.KEY_STOP_REMIND)
    pass  # Unknown
    # PlayerPrefs.GetInt(uv0.KEY_NEWLY_ID)
    pass  # Unknown

    # /model/proxy/serverproxy.lua
    # PlayerPrefs.GetInt("server.id" .. slot1)
    server_id = Field(formatter=int, default=0, regex='server.id(.*)')
    # PlayerPrefs.GetString("loginedServer_" .. slot1)
    loginedServer = Field(formatter=str, default='', regex='loginedServer_(.*)')

    # /model/proxy/settingsproxy.lua
    # PlayerPrefs.GetInt("ShipSkinBGM", 1)
    ShipSkinBGM = Field(formatter=int, default=1, regex='ShipSkinBGM')
    # PlayerPrefs.GetInt("disableBG", 1)
    disableBG = Field(formatter=int, default=1, regex='disableBG')
    # PlayerPrefs.GetInt("disableLive2d", 1)
    disableLive2d = Field(formatter=int, default=1, regex='disableLive2d')
    # PlayerPrefs.GetInt("playerShipId")
    playerShipId = Field(formatter=int, default=0, regex='playerShipId')
    # PlayerPrefs.GetString("backyardRemind")
    backyardRemind = Field(formatter=str, default='', regex='backyardRemind')
    # PlayerPrefs.GetInt("userAgreement", 0)
    userAgreement = Field(formatter=int, default=0, regex='userAgreement')
    # PlayerPrefs.GetInt("maxLevelHelp", 0)
    maxLevelHelp = Field(formatter=int, default=0, regex='maxLevelHelp')
    # PlayerPrefs.GetInt("AutoBattleTip", 0)
    AutoBattleTip = Field(formatter=int, default=0, regex='AutoBattleTip')
    # PlayerPrefs.GetInt("setFlagShip", 0)
    setFlagShip = Field(formatter=int, default=0, regex='setFlagShip')
    # PlayerPrefs.GetInt("setFlagShipforskinatlas", 0)
    setFlagShipforskinatlas = Field(formatter=int, default=0, regex='setFlagShipforskinatlas')
    # PlayerPrefs.GetFloat("SetScreenRatio", ADAPT_TARGET)
    SetScreenRatio = Field(formatter=float, default=0.0, regex='SetScreenRatio')
    # PlayerPrefs.GetInt("story_autoplay_flag", 0)
    story_autoplay_flag = Field(formatter=int, default=0, regex='story_autoplay_flag')
    # PlayerPrefs.GetInt("collection_Help", 0)
    collection_Help = Field(formatter=int, default=0, regex='collection_Help')
    # PlayerPrefs.GetInt("main_scene_word_toggle", 1)
    main_scene_word_toggle = Field(formatter=int, default=1, regex='main_scene_word_toggle')
    # PlayerPrefs.GetInt("worldBossFlag" .. slot1, 1)
    worldBossFlag = Field(formatter=int, default=1, regex='worldBossFlag(.*)')
    # PlayerPrefs.GetInt("world_flag_" .. slot1, 0)
    world_flag = Field(formatter=int, default=0, regex='world_flag_(.*)')
    # PlayerPrefs.GetInt("DockYardLockFlag" .. getProxy(PlayerProxy):getRawData().id, 0)
    DockYardLockFlag = Field(formatter=int, default=0, regex='DockYardLockFlag(.*)')
    # PlayerPrefs.GetInt("DockYardLevelFlag" .. getProxy(PlayerProxy):getRawData().id, 0)
    DockYardLevelFlag = Field(formatter=int, default=0, regex='DockYardLevelFlag(.*)')
    # PlayerPrefs.GetFloat(tostring(slot1) .. "_x", 0)
    x = Field(formatter=float, default=0.0, regex='(.*)_x')
    # PlayerPrefs.GetInt(tostring(slot1) .. "_" .. slot2, 1)
    pass  # Unknown
    # PlayerPrefs.GetInt("currentSecretaryIndex", 1)
    currentSecretaryIndex = Field(formatter=int, default=1, regex='currentSecretaryIndex')
    # PlayerPrefs.GetInt("currentSecretaryIndex", 1)
    pass  # Duplicate
    # PlayerPrefs.GetInt(slot1, 0)
    pass  # Unknown
    # PlayerPrefs.GetInt(slot1, 0)
    pass  # Unknown
    # PlayerPrefs.GetString("HitMonsterNianLayer2020" .. getProxy(PlayerProxy):getRawData().id, "0")
    HitMonsterNianLayer2020 = Field(formatter=str, default='0', regex='HitMonsterNianLayer2020(.*)')
    # PlayerPrefs.GetInt("event_act_help1" .. getProxy(PlayerProxy):getRawData().id, 0)
    event_act_help1 = Field(formatter=int, default=0, regex='event_act_help1(.*)')
    # PlayerPrefs.GetInt("story_speed_flag" .. ((not getProxy(PlayerProxy) or getProxy(PlayerProxy):getRawData().id) and 1), 0)
    story_speed_flag = Field(formatter=int, default=0, regex='story_speed_flag(.*)')
    # PlayerPrefs.GetInt("tipLimitSkinShopTime_", 0)
    tipLimitSkinShopTime = Field(formatter=int, default=0, regex='tipLimitSkinShopTime_')
    # PlayerPrefs.GetString("_WorldBossProgressTipFlag_", slot1[1] .. "&" .. slot1[1] + slot1[2])
    WorldBossProgressTipFlag = Field(formatter=str, default='slot1[1] .. "&" .. slot1[1] + slot1[2]', regex='_WorldBossProgressTipFlag_')
    # PlayerPrefs.GetInt("chat__setting", IndexConst.Flags2Bits(slot1))
    chat__setting = Field(formatter=int, default=0, regex='chat__setting')
    # PlayerPrefs.GetString("commander_play_sortdata", "Rarity#0")
    commander_play_sortdata = Field(formatter=str, default='Rarity#0', regex='commander_play_sortdata')
    # PlayerPrefs.GetInt("ActivityMapSPTip" .. getProxy(PlayerProxy):getRawData().id, 0)
    ActivityMapSPTip = Field(formatter=int, default=0, regex='ActivityMapSPTip(.*)')
    # PlayerPrefs.GetInt(getProxy(PlayerProxy):getRawData().id .. "IsTipNewTheme" .. slot2, 0)
    IsTipNewTheme = Field(formatter=int, default=0, regex='(.*)IsTipNewTheme(.*)')
    # PlayerPrefs.GetString(getProxy(PlayerProxy):getRawData().id .. "IsTipNewGenFurniture")
    IsTipNewGenFurniture = Field(formatter=str, default='', regex='(.*)IsTipNewGenFurniture')

    # /model/proxy/technologyproxy.lua
    # PlayerPrefs.GetInt("technology_version")
    technology_version = Field(formatter=int, default=0, regex='technology_version')

    # /model/proxy/userproxy.lua
    # PlayerPrefs.GetString("user.type")
    user_type = Field(formatter=str, default='', regex='user.type')
    # PlayerPrefs.GetString("user.arg2")
    user_arg2 = Field(formatter=str, default='', regex='user.arg2')
    # PlayerPrefs.GetString("user.arg3")
    user_arg3 = Field(formatter=str, default='', regex='user.arg3')
    # PlayerPrefs.GetString("user.arg1")
    user_arg1 = Field(formatter=str, default='', regex='user.arg1')
    # PlayerPrefs.GetString("transcode")
    transcode = Field(formatter=str, default='', regex='transcode')
    # PlayerPrefs.GetInt(uv0 .. slot1, PLATFORM)
    pass  # Unknown
    # PlayerPrefs.GetInt(uv0 .. slot1, PLATFORM)
    pass  # Unknown

    # /model/proxy/worldproxy.lua
    # PlayerPrefs.GetInt("world_skip_battle")
    world_skip_battle = Field(formatter=int, default=0, regex='world_skip_battle')

    # /model/vo/activity.lua
    # PlayerPrefs.GetInt("ACTIVITY_TYPE_EVENT_" .. slot0.id .. "_" .. getProxy(PlayerProxy):getData().id)
    ACTIVITY_TYPE_EVENT = Field(formatter=int, default=0, regex='ACTIVITY_TYPE_EVENT_(.*)_(.*)')

    # /model/vo/chapter.lua
    # PlayerPrefs.GetInt("chapter_quickPlay_flag_" .. slot0.id, 0)
    chapter_quickPlay_flag = Field(formatter=int, default=0, regex='chapter_quickPlay_flag_(.*)')
    # PlayerPrefs.GetInt(uv0.GetChapterLastFleetCacheKey(slot0), 0)
    pass  # Unknown

    # /model/vo/chapterfleet.lua
    # PlayerPrefs.GetInt("team_formation_" .. slot0.id, 1)
    team_formation = Field(formatter=int, default=1, regex='team_formation_(.*)')

    # /model/vo/eventinfo.lua
    # PlayerPrefs.GetString(uv0 .. slot1:getRawData().id)
    pass  # Unknown

    # /model/vo/ship.lua
    # PlayerPrefs.GetInt("paint_hide_other_obj_" .. slot2.painting, 0)
    paint_hide_other_obj = Field(formatter=int, default=0, regex='paint_hide_other_obj_(.*)')
    # PlayerPrefs.GetString("equipment_record" .. "_" .. slot1 .. "_" .. slot0.id)
    equipment_record = Field(formatter=str, default='', regex='equipment_record_(.*)_(.*)')

    # /model/vo/guild/events/guildmission.lua
    # PlayerPrefs.GetInt("guild_mission_formation_tip" .. slot0.configId, 0)
    guild_mission_formation_tip = Field(formatter=int, default=0, regex='guild_mission_formation_tip(.*)')

    # /model/vo/notice/notice.lua
    # PlayerPrefs.GetInt(slot0:prefKey())
    pass  # Unknown

    # /support/helpers/m02.lua
    # PlayerPrefs.GetInt("paint_hide_other_obj_" .. slot1, 0)
    pass  # Duplicate
    # PlayerPrefs.GetInt("paint_hide_other_obj_" .. slot1, 0)
    pass  # Duplicate

    # /support/utils/hxset.lua
    # PlayerPrefs.GetInt(uv0.codeModeKey)
    pass  # Unknown
    # PlayerPrefs.GetInt("localization_use", 0)
    localization_use = Field(formatter=int, default=0, regex='localization_use')

    # /view/activity/activitymediator.lua
    # PlayerPrefs.GetString("permanent_time", "")
    pass  # Duplicate

    # /view/activity/activitypermanentlayer.lua
    # PlayerPrefs.GetInt("permanent_select", 0)
    permanent_select = Field(formatter=int, default=0, regex='permanent_select')

    # /view/activity/airforceofdragonemperyui.lua
    # PlayerPrefs.GetInt("AirFightIndex_" .. getProxy(PlayerProxy):getRawData().id, 1)
    AirFightIndex = Field(formatter=int, default=1, regex='AirFightIndex_(.*)')

    # /view/activity/crusingscene.lua
    # PlayerPrefs.GetInt(string.format("crusing_%d_phase_display", slot0.activity.id), 0)
    crusing__d_phase_display = Field(formatter=int, default=0, regex='crusing_%d_phase_display')

    # /view/activity/crusingtasklayer.lua
    # PlayerPrefs.GetInt(string.format("cursing_%d_task_week_%d", slot0.activity.id, slot5), 0)
    cursing__d_task_week__d = Field(formatter=int, default=0, regex='cursing_%d_task_week_%d')

    # /view/activity/refluxmediator.lua
    # PlayerPrefs.GetInt(slot6.id .. "_" .. slot2.data2)
    pass  # Unknown

    # /view/activity/banaiactivity/blackwhitegridlayer.lua
    # PlayerPrefs.GetString("BlackWhiteGridMapData-" .. slot1.id .. "-" .. slot0.player.id, "")
    BlackWhiteGridMapData = Field(formatter=str, default='', regex='BlackWhiteGridMapData-(.*)-(.*)')
    # PlayerPrefs.GetInt("BlackWhiteGridMapIndex-" .. slot0.player.id, 1)
    BlackWhiteGridMapIndex = Field(formatter=int, default=1, regex='BlackWhiteGridMapIndex-(.*)')

    # /view/activity/decodegame/game/decodegameview.lua
    # PlayerPrefs.GetInt("DecodeGameHelpBg" .. getProxy(PlayerProxy):getRawData().id .. slot1, 0)
    DecodeGameHelpBg = Field(formatter=int, default=0, regex='DecodeGameHelpBg(.*)(.*)')

    # /view/activity/fushunadventure/fushunadventuregame.lua
    # PlayerPrefs.GetInt("FushunAdventureGame" .. getProxy(PlayerProxy):getRawData().id, 0)
    FushunAdventureGame = Field(formatter=int, default=0, regex='FushunAdventureGame(.*)')

    # /view/activity/lanternriddlesview/lanternriddlesmodel.lua
    # PlayerPrefs.GetInt(slot0 .. "_" .. slot1 .. "_" .. uv0, 0)
    pass  # Unknown

    # /view/activity/newservercarnival/newservercarnivalscene.lua
    # PlayerPrefs.GetInt("newserver_shop_first_" .. slot0.player.id)
    newserver_shop_first = Field(formatter=int, default=0, regex='newserver_shop_first_(.*)')

    # /view/activity/newservercarnival/newservergiftpage.lua
    # PlayerPrefs.GetInt("newserver_gift_first_" .. slot0.playerId)
    newserver_gift_first = Field(formatter=int, default=0, regex='newserver_gift_first_(.*)')

    # /view/activity/subpages/aprilfooldiscoveryrepage.lua
    # PlayerPrefs.GetInt("SuperBurinPopUp_" .. getProxy(PlayerProxy):getRawData().id, 0)
    SuperBurinPopUp = Field(formatter=int, default=0, regex='SuperBurinPopUp_(.*)')

    # /view/activity/subpages/collectioneventptpage.lua
    # PlayerPrefs.GetInt("ACTIVITY_TYPE_EVENT_" .. slot0.activity.id .. "_" .. getProxy(PlayerProxy):getData().id)
    pass  # Duplicate

    # /view/activity/subpages/crusingdisplayactpage.lua
    # PlayerPrefs.GetInt("first_crusing_page_display:" .. uv0.activity.id, 0)
    first_crusing_page_display = Field(formatter=int, default=0, regex='first_crusing_page_display:(.*)')

    # /view/activity/subpages/icecreamptpage.lua
    # PlayerPrefs.GetInt(uv0.Icecream_Save_Tag_Pre .. slot4, 0)
    pass  # Unknown

    # /view/activity/subpages/jiujiuyoyopage.lua
    # PlayerPrefs.GetInt("jiujiuyoyo_first_" .. getProxy(PlayerProxy):getData().id)
    jiujiuyoyo_first = Field(formatter=int, default=0, regex='jiujiuyoyo_first_(.*)')

    # /view/activity/subpages/kfcptpage.lua
    # PlayerPrefs.GetInt("kfc_pt_" .. slot0.playerId .. "_day_" .. slot0.curDay)
    kfc_pt = Field(formatter=int, default=0, regex='kfc_pt_(.*)_day_(.*)')

    # /view/activity/subpages/pizzahutptpage.lua
    # PlayerPrefs.GetInt(uv0.Pizza_Save_Tag_Pre .. slot4, 0)
    pass  # Unknown

    # /view/activity/subpages/pockyskinpage.lua
    # PlayerPrefs.GetInt("PockySkinSignDay" .. (getProxy(PlayerProxy):getRawData().id or "-1"), 0)
    PockySkinSignDay = Field(formatter=int, default=0, regex='PockySkinSignDay-1')

    # /view/activity/subpages/wwfptpage.lua
    # PlayerPrefs.GetInt("wwf_first_" .. slot0.playerId)
    wwf_first = Field(formatter=int, default=0, regex='wwf_first_(.*)')
    # PlayerPrefs.GetInt("wwf_select_index_" .. slot0.playerId)
    wwf_select_index = Field(formatter=int, default=0, regex='wwf_select_index_(.*)')
    # PlayerPrefs.GetInt("wwf_select_index_" .. slot0.playerId)
    pass  # Duplicate
    # PlayerPrefs.GetInt("wwf_todo_task_num_" .. slot0.playerId)
    wwf_todo_task_num = Field(formatter=int, default=0, regex='wwf_todo_task_num_(.*)')
    # PlayerPrefs.GetInt("wwf_todo_task_num_" .. getProxy(PlayerProxy):getData().id)
    pass  # Duplicate

    # /view/activity/worldinpicture/worldinpicturescene.lua
    # PlayerPrefs.GetString("WorldInPictureScene_1" .. getProxy(PlayerProxy):getRawData().id, "0#0")
    WorldInPictureScene_1 = Field(formatter=str, default='0#0', regex='WorldInPictureScene_1(.*)')

    # /view/battle/battleresultlayer.lua
    # PlayerPrefs.GetInt(DISPLAY_SHIP_GET_EFFECT)
    pass  # Unknown

    # /view/battle/battleresultmediator.lua
    # PlayerPrefs.GetInt(AUTO_BATTLE_LABEL, 0)
    pass  # Unknown

    # /view/battle/battleworldbossresultlayer.lua
    # PlayerPrefs.GetInt(DISPLAY_SHIP_GET_EFFECT)
    pass  # Unknown

    # /view/battle/combatloadui.lua
    # PlayerPrefs.GetInt("bgFitMode", 0)
    bgFitMode = Field(formatter=int, default=0, regex='bgFitMode')

    # /view/battle/dailylevelscene.lua
    # PlayerPrefs.GetInt("daily_level_quick_battle_tip", 0)
    daily_level_quick_battle_tip = Field(formatter=int, default=0, regex='daily_level_quick_battle_tip')

    # /view/battle/levelmediator2.lua
    # PlayerPrefs.GetInt("chapter_submarine_ai_type_" .. getProxy(PlayerProxy):getRawData().id)
    chapter_submarine_ai_type = Field(formatter=int, default=0, regex='chapter_submarine_ai_type_(.*)')

    # /view/battle/levelscene.lua
    # PlayerPrefs.GetInt("ex_mapId")
    ex_mapId = Field(formatter=int, default=0, regex='ex_mapId')
    # PlayerPrefs.GetString("remaster_tip")
    remaster_tip = Field(formatter=str, default='', regex='remaster_tip')
    # PlayerPrefs.GetInt("chapter_autofight_flag_" .. uv2.id, 1)
    chapter_autofight_flag = Field(formatter=int, default=1, regex='chapter_autofight_flag_(.*)')

    # /view/collection/galleryconst.lua
    # PlayerPrefs.GetInt(uv0.Set_BG_Func_Save_Tag .. getProxy(PlayerProxy):getRawData().id)
    pass  # Unknown

    # /view/equipment/transformation/equipmenttransformtreescene.lua
    # PlayerPrefs.GetInt("ShowTransformTip_" .. slot2[3], 0)
    ShowTransformTip = Field(formatter=int, default=0, regex='ShowTransformTip_(.*)')

    # /view/helper/shipwordhelper.lua
    # PlayerPrefs.GetInt(CV_LANGUAGE_KEY .. uv0[slot0].ship_group)
    pass  # Unknown

    # /view/helper/tagtiphelper.lua
    # PlayerPrefs.GetInt("Ever_Enter_Mall_", 0)
    Ever_Enter_Mall = Field(formatter=int, default=0, regex='Ever_Enter_Mall_')
    # PlayerPrefs.GetInt("Ever_Enter_Skin_Shop_", 0)
    Ever_Enter_Skin_Shop = Field(formatter=int, default=0, regex='Ever_Enter_Skin_Shop_')
    # PlayerPrefs.GetInt("Tec_Ship_Gift_Enter_Tag", 0)
    Tec_Ship_Gift_Enter_Tag = Field(formatter=int, default=0, regex='Tec_Ship_Gift_Enter_Tag')

    # /view/level/levelfleetview.lua
    # PlayerPrefs.GetInt("autoFight_firstUse_sp", 0)
    autoFight_firstUse_sp = Field(formatter=int, default=0, regex='autoFight_firstUse_sp')
    # PlayerPrefs.GetInt(uv0, 1)
    pass  # Unknown
    # PlayerPrefs.GetInt(uv0, 1)
    pass  # Unknown
    # PlayerPrefs.GetInt("lastFleetDuty_" .. (slot0.chapter.id or 0), 0)
    lastFleetDuty = Field(formatter=int, default=0, regex='lastFleetDuty_(.*)')
    # PlayerPrefs.GetInt("SPOPItemReminder")
    SPOPItemReminder = Field(formatter=int, default=0, regex='SPOPItemReminder')
    # PlayerPrefs.GetInt("lastFleetDuty_" .. (slot0.chapter.id or 0), 0)
    pass  # Duplicate
    # PlayerPrefs.GetInt("autoFight_firstUse_sp", 0)
    pass  # Duplicate
    # PlayerPrefs.GetInt(uv0, 1)
    pass  # Unknown
    # PlayerPrefs.GetInt(uv0, 1)
    pass  # Unknown
    # PlayerPrefs.GetInt(Chapter.GetSPOperationItemCacheKey(slot0.chapter.id), 0)
    pass  # Unknown

    # /view/level/levelinfoview.lua
    # PlayerPrefs.GetInt("chapter_loop_flag_" .. slot1.id, -1)
    chapter_loop_flag = Field(formatter=int, default=-1, regex='chapter_loop_flag_(.*)')
    # PlayerPrefs.GetInt("chapter_autofight_flag_" .. slot1.id, 1)
    pass  # Duplicate
    # PlayerPrefs.GetInt("chapter_quickPlay_flag_" .. slot1.id, 0)
    pass  # Duplicate

    # /view/level/leveloperationitempanel.lua
    # PlayerPrefs.GetInt("extraOperationItemID", 0)
    extraOperationItemID = Field(formatter=int, default=0, regex='extraOperationItemID')

    # /view/level/levelremasterview.lua
    # PlayerPrefs.GetInt(slot4, slot5)
    pass  # Unknown

    # /view/level/levelstagetotalrewardpanel.lua
    # PlayerPrefs.GetInt(AUTO_BATTLE_LABEL, 0)
    pass  # Unknown
    # PlayerPrefs.GetInt("autoFight_firstUse_sp", 0)
    pass  # Duplicate

    # /view/level/levelstageview.lua
    # PlayerPrefs.GetInt(slot6, 1)
    pass  # Unknown
    # PlayerPrefs.GetInt("help_displayed_on_" .. uv1.id, 0)
    help_displayed_on = Field(formatter=int, default=0, regex='help_displayed_on_(.*)')

    # /view/login/loginscene.lua
    # PlayerPrefs.GetString("op_ver", "")
    op_ver = Field(formatter=str, default='', regex='op_ver')

    # /view/main/trainingcampscene.lua
    # PlayerPrefs.GetInt("TrainCamp_Tec_Catchup_First_Tag", 0)
    TrainCamp_Tec_Catchup_First_Tag = Field(formatter=int, default=0, regex='TrainCamp_Tec_Catchup_First_Tag')

    # /view/minigame/gameview/decodeminigameview.lua
    # PlayerPrefs.GetInt("DecodeGameMapId", 1)
    DecodeGameMapId = Field(formatter=int, default=1, regex='DecodeGameMapId')

    # /view/minigame/gameview/musicgameview.lua
    # PlayerPrefs.GetInt("musicgame_first_" .. getProxy(PlayerProxy):getData().id)
    musicgame_first = Field(formatter=int, default=0, regex='musicgame_first_(.*)')
    # PlayerPrefs.GetInt("musicgame_idol_speed")
    musicgame_idol_speed = Field(formatter=int, default=0, regex='musicgame_idol_speed')

    # /view/minigame/gameview/qtegameview.lua
    # PlayerPrefs.GetInt("QTEGameGuide", 0)
    QTEGameGuide = Field(formatter=int, default=0, regex='QTEGameGuide')

    # /view/minigame/gameview/volleyballgameview.lua
    # PlayerPrefs.GetInt("volleyballgame_first_" .. getProxy(PlayerProxy):getData().id)
    volleyballgame_first = Field(formatter=int, default=0, regex='volleyballgame_first_(.*)')

    # /view/msgboxsubpanel/monthcardoutdatetippanel.lua
    # PlayerPrefs.GetInt("MonthCardEndDate" .. slot0.id, 0)
    MonthCardEndDate = Field(formatter=int, default=0, regex='MonthCardEndDate(.*)')
    # PlayerPrefs.GetInt("MonthCardTipDate" .. slot0.id, 0)
    MonthCardTipDate = Field(formatter=int, default=0, regex='MonthCardTipDate(.*)')
    # PlayerPrefs.GetInt("MonthCardTagDate" .. slot0.id, 0)
    MonthCardTagDate = Field(formatter=int, default=0, regex='MonthCardTagDate(.*)')

    # /view/newmain/sequence/maincrusingactsequence.lua
    # PlayerPrefs.GetInt("cursing_first_enter_scene:" .. slot3.id, 0)
    cursing_first_enter_scene = Field(formatter=int, default=0, regex='cursing_first_enter_scene:(.*)')
    # PlayerPrefs.GetInt(string.format("crusing_%d_last_time", slot1.id), 3)
    crusing__d_last_time = Field(formatter=int, default=0, regex='crusing_%d_last_time')

    # /view/newmain/sequence/mainequipmentchangesequence.lua
    # PlayerPrefs.GetInt("ItemIconChange_" .. slot2.equipID, 0)
    ItemIconChange = Field(formatter=int, default=0, regex='ItemIconChange_(.*)')

    # /view/newmain/view/mainchatroomview.lua
    # PlayerPrefs.GetInt(HIDE_CHAT_FLAG)
    pass  # Unknown
    # PlayerPrefs.GetInt(HIDE_CHAT_FLAG)
    pass  # Unknown

    # /view/newmain/view/mainpaintingview.lua
    # PlayerPrefs.GetInt("paint_hide_other_obj_" .. slot0.painting.paintingName, 0)
    pass  # Duplicate
    # PlayerPrefs.GetInt("paint_hide_other_obj_" .. slot0.painting.paintingName, 0)
    pass  # Duplicate

    # /view/setting/newsettingsscene.lua
    # PlayerPrefs.GetFloat("firstIntoOtherPanel")
    pass  # Duplicate

    # /view/setting/pages/settingsbattlepage.lua
    # PlayerPrefs.GetFloat(slot2, slot4.x)
    pass  # Unknown
    # PlayerPrefs.GetFloat(slot3, slot4.y)
    pass  # Unknown

    # /view/setting/pages/settingsotherpage.lua
    # PlayerPrefs.GetFloat("firstIntoOtherPanel")
    pass  # Duplicate

    # /view/setting/panels/settingsfpspanle.lua
    # PlayerPrefs.GetInt("fps_limit", DevicePerformanceUtil.GetDefaultFps())
    fps_limit = Field(formatter=int, default=0, regex='fps_limit')

    # /view/setting/panels/settingsotherpanel.lua
    # PlayerPrefs.GetInt("AUTOFIGHT_BATTERY_SAVEMODE", 0)
    AUTOFIGHT_BATTERY_SAVEMODE = Field(formatter=int, default=0, regex='AUTOFIGHT_BATTERY_SAVEMODE')
    # PlayerPrefs.GetInt(_G[slot1.name], slot1.default or 0)
    pass  # Unknown

    # /view/setting/panels/settingssecondpasswordpanle.lua
    # PlayerPrefs.GetFloat("firstOpenSecondaryPassword")
    firstOpenSecondaryPassword = Field(formatter=float, default=0.0, regex='firstOpenSecondaryPassword')

    # /view/setting/panels/settingssoundpanle.lua
    # PlayerPrefs.GetInt("mute_audio", 0)
    mute_audio = Field(formatter=int, default=0, regex='mute_audio')
    # PlayerPrefs.GetFloat("bgm_vol_mute_setting", DEFAULT_BGMVOLUME)
    bgm_vol_mute_setting = Field(formatter=float, default=0.0, regex='bgm_vol_mute_setting')
    # PlayerPrefs.GetFloat("se_vol_mute_setting", DEFAULT_SEVOLUME)
    se_vol_mute_setting = Field(formatter=float, default=0.0, regex='se_vol_mute_setting')
    # PlayerPrefs.GetFloat("cv_vol_mute_setting", DEFAULT_CVVOLUME)
    cv_vol_mute_setting = Field(formatter=float, default=0.0, regex='cv_vol_mute_setting')
    # PlayerPrefs.GetFloat("bgm_vol_mute_setting", DEFAULT_BGMVOLUME)
    pass  # Duplicate
    # PlayerPrefs.GetFloat("se_vol_mute_setting", DEFAULT_SEVOLUME)
    pass  # Duplicate
    # PlayerPrefs.GetFloat("cv_vol_mute_setting", DEFAULT_CVVOLUME)
    pass  # Duplicate

    # /view/ship/dockyardquickselectsettingpage.lua
    # PlayerPrefs.GetString("QuickSelectWithoutMaxstar", "KeepAll")
    QuickSelectWithoutMaxstar = Field(formatter=str, default='KeepAll', regex='QuickSelectWithoutMaxstar')
    # PlayerPrefs.GetString("QuickSelectWhenHasAtLeastOneMaxstar", "KeepNone")
    QuickSelectWhenHasAtLeastOneMaxstar = Field(formatter=str, default='KeepNone', regex='QuickSelectWhenHasAtLeastOneMaxstar')
    # PlayerPrefs.GetInt("QuickSelectRarity1", 3)
    QuickSelectRarity1 = Field(formatter=int, default=3, regex='QuickSelectRarity1')
    # PlayerPrefs.GetInt("QuickSelectRarity2", 4)
    QuickSelectRarity2 = Field(formatter=int, default=4, regex='QuickSelectRarity2')
    # PlayerPrefs.GetInt("QuickSelectRarity3", 2)
    QuickSelectRarity3 = Field(formatter=int, default=2, regex='QuickSelectRarity3')

    # /view/ship/dockyardscene.lua
    # PlayerPrefs.GetInt("QuickSelectRarity1", 3)
    pass  # Duplicate
    # PlayerPrefs.GetInt("QuickSelectRarity2", 4)
    pass  # Duplicate
    # PlayerPrefs.GetInt("QuickSelectRarity3", 2)
    pass  # Duplicate
    # PlayerPrefs.GetString("QuickSelectWhenHasAtLeastOneMaxstar", "KeepNone")
    pass  # Duplicate
    # PlayerPrefs.GetString("QuickSelectWithoutMaxstar", "KeepAll")
    pass  # Duplicate

    # /view/ship/live2d.lua
    # PlayerPrefs.GetInt(GYRO_ENABLE, 1)
    pass  # Unknown
    # PlayerPrefs.GetInt(GYRO_ENABLE, 1)
    pass  # Unknown

    # /view/ship/newshiplayer.lua
    # PlayerPrefs.GetInt(RARE_SHIP_VIBRATE, 1)
    pass  # Unknown

    # /view/ship/proposeui.lua
    # PlayerPrefs.GetInt("paint_hide_other_obj_" .. slot1, 0)
    pass  # Duplicate

    # /view/ship/shipskincard.lua
    # PlayerPrefs.GetInt("paint_hide_other_obj_" .. slot0.paintingName, 0)
    pass  # Duplicate

    # /view/ship/shipinfoview/shipdetailview.lua
    # PlayerPrefs.GetInt("QUICK_CHANGE_EQUIP", 1)
    QUICK_CHANGE_EQUIP = Field(formatter=int, default=1, regex='QUICK_CHANGE_EQUIP')

    # /view/ship/shipinfoview/shipfashionview.lua
    # PlayerPrefs.GetInt("paint_hide_other_obj_" .. uv2.paintingName, 0)
    pass  # Duplicate

    # /view/ship/shipprofileview/shipprofilescene.lua
    # PlayerPrefs.GetInt("paint_hide_other_obj_" .. slot0.skin.painting, 0)
    pass  # Duplicate

    # /view/shops/pages/newservershoppage.lua
    # PlayerPrefs.GetInt("newserver_shop_phase_" .. slot1 .. "_" .. slot0.playerId)
    newserver_shop_phase = Field(formatter=int, default=0, regex='newserver_shop_phase_(.*)_(.*)')
    # PlayerPrefs.GetInt("newserver_shop_first_" .. slot0.playerId)
    pass  # Duplicate

    # /view/snapshot/snapshotscene.lua
    # PlayerPrefs.GetInt("hadShowForVideoTip")
    hadShowForVideoTip = Field(formatter=int, default=0, regex='hadShowForVideoTip')
    # PlayerPrefs.GetInt(SHOW_TOUCH_EFFECT, 1)
    pass  # Unknown

    # /view/snapshot/snapshotsharelayer.lua
    # PlayerPrefs.GetInt("snapshotAgress")
    snapshotAgress = Field(formatter=int, default=0, regex='snapshotAgress')

    # /view/technology/technologysettingslayer.lua
    # PlayerPrefs.GetInt("isShowFinishCatchupVersion")
    isShowFinishCatchupVersion = Field(formatter=int, default=0, regex='isShowFinishCatchupVersion')

    # /view/world/worldscene.lua
    # PlayerPrefs.GetInt("first_auto_fight_mark", 0)
    first_auto_fight_mark = Field(formatter=int, default=0, regex='first_auto_fight_mark')
    # PlayerPrefs.GetInt("world_sub_auto_call", 0)
    pass  # Duplicate
    # PlayerPrefs.GetInt("world_sub_call_line", 0)
    pass  # Duplicate
    # PlayerPrefs.GetInt("auto_switch_mode", 0)
    pass  # Duplicate

    # /view/world/worldswitchplanninglayer.lua
    # PlayerPrefs.GetString("auto_switch_difficult_safe", "all")
    pass  # Duplicate
    # PlayerPrefs.GetInt("auto_switch_wait", 0)
    auto_switch_wait = Field(formatter=int, default=0, regex='auto_switch_wait')
    # PlayerPrefs.GetInt("auto_switch_wait_2", 0)
    auto_switch_wait_2 = Field(formatter=int, default=0, regex='auto_switch_wait_2')
    # PlayerPrefs.GetInt("auto_switch_mode", 0)
    pass  # Duplicate
    # PlayerPrefs.GetString(slot6, slot7)
    pass  # Unknown

    # /view/world/worldmediacollection/worldmediacollectionmemorygrouplayer.lua
    # PlayerPrefs.GetInt("MEMORY_GROUP_NOTIFICATION" .. getProxy(PlayerProxy):getRawData().id .. " " .. slot3.id, 0)
    pass  # Duplicate
    # PlayerPrefs.GetInt("MEMORY_GROUP_NOTIFICATION" .. slot2 .. " " .. slot7.id, 0)
    pass  # Duplicate
